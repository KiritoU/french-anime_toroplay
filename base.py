import logging

from bs4 import BeautifulSoup

from helper import helper
from settings import CONFIG
from toroplay import Toroplay

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)


class Crawler:
    def crawl_soup(self, url):
        logging.info(f"Crawling {url}")

        html = helper.download_url(url)
        soup = BeautifulSoup(html.content, "html.parser")

        return soup

    def get_film_links(
        self,
        soup: BeautifulSoup,
        post_type: str = "series",
    ) -> dict:
        film_links = {}
        # if post_type == "series":
        eps = soup.find("div", class_="eps")
        if eps:
            episodes = eps.text.split("\n")
            for episode in episodes:
                episode_name, links = episode.split("!")
                film_links[episode_name] = links.split(",")

        return film_links

    def crawl_film(
        self,
        href: str,
        title: str = "",
        cover_img_src: str = "",
        post_type: str = "series",
    ):
        soup = self.crawl_soup(href)

        if not title:
            title = helper.get_title(soup)

        if not cover_img_src:
            cover_img_src = helper.get_cover_img_src(soup)

        trailer_id = helper.get_trailer_id(soup)
        extra_info = helper.get_extra_info_from(soup=soup)

        description = extra_info.get("synopsis", "")

        if not title:
            helper.error_log(
                msg=f"No title was found\n{href}", log_file="base.no_title.log"
            )
            return

        film_data = {
            "title": title,
            "description": description,
            "post_type": post_type,
            "trailer_id": trailer_id,
            "fondo_player": cover_img_src,
            "poster_url": cover_img_src,
            "extra_info": extra_info,
        }

        film_links = self.get_film_links(soup, post_type)
        return [film_data, film_links]

    def crawl_page(self, url: str = CONFIG.FRENCH_ANIME_VF, post_type: str = "series"):
        soup = self.crawl_soup(url)
        if not soup:
            return 0

        dle_content = soup.find("div", {"id": "dle-content"})
        if not dle_content:
            return 0

        movs = dle_content.find_all("div", class_="mov")
        if not movs:
            return 0

        for mov in movs:
            try:
                a_element = mov.find("a", class_="mov-t")

                href = a_element.get("href")
                if "http" not in href:
                    href = CONFIG.FRENCH_ANIME_HOMEPAGE + href

                title = (
                    "" if not a_element else a_element.text.replace("\n", "").strip()
                )

                try:
                    cover_img_src = mov.find("div", class_="mov-i").find("img")
                    cover_img_src = cover_img_src.get("src")
                    if "http" not in cover_img_src:
                        cover_img_src = CONFIG.FRENCH_ANIME_HOMEPAGE + cover_img_src
                except Exception as e:
                    cover_img_src = ""

                try:
                    nbloc1_2 = mov.find("div", class_="nbloc1-2")
                    season_str = nbloc1_2.text
                except:
                    season_str = ""

                # print("|".join([href, title, cover_img_src]))

                film_data, film_links = self.crawl_film(
                    href=href,
                    title=title,
                    cover_img_src=cover_img_src,
                    post_type=post_type,
                )

                Toroplay(film_data, film_links, season_str=season_str).insert_film()
            except Exception as e:
                helper.error_log(f"Failed to get href\n{mov}\n{e}", "page.log")

        return 1

    def crawl_homepage(
        self, url: str = CONFIG.FRENCH_ANIME_HOMEPAGE, post_type: str = "series"
    ):
        soup = self.crawl_soup(url)
        if not soup:
            return 0

        for class_name in ["lastserieadd", "lastfilmadd"]:
            last_add = soup.find("div", class_=class_name)
            if not last_add:
                continue

            lis = last_add.find_all("li")
            if not lis:
                continue

            for li in lis:
                try:
                    a_element = li.find("a")

                    href = a_element.get("href")
                    if "http" not in href:
                        href = CONFIG.FRENCH_ANIME_HOMEPAGE + href

                    season_str = a_element.text

                    print(" | ".join([href, season_str]))

                    film_data, film_links = self.crawl_film(
                        href=href,
                        post_type=post_type,
                    )

                    Toroplay(film_data, film_links, season_str=season_str).insert_film()
                except Exception as e:
                    helper.error_log(f"Failed to get href\n{li}\n{e}", "page.log")

        return 1


if __name__ == "__main__":
    Crawler().crawl_homepage()
    # Crawler().crawl_page(url=CONFIG.FRENCH_ANIME_VF + "/page/14")
    # Crawler().crawl_page(url=CONFIG.FRENCH_ANIME_FILMS + "/page/14", post_type="movies")
