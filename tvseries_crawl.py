import logging
import time

from base import Crawler
from settings import CONFIG

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)

crawler = Crawler()

if __name__ == "__main__":
    while True:
        vf_page = 1
        while True:
            try:
                crawled_page = crawler.crawl_page(
                    f"{CONFIG.FRENCH_ANIME_VF}/page/{vf_page}/"
                )
                if not crawled_page and vf_page >= CONFIG.FRENCH_ANIME_VF_LAST_PAGE:
                    break

                vf_page += 1
            except Exception as e:
                break
            time.sleep(CONFIG.WAIT_BETWEEN_ALL)

        vostfr_page = 1
        while True:
            try:
                crawled_page = crawler.crawl_page(
                    f"{CONFIG.FRENCH_ANIME_VOSTFR}/page/{vostfr_page}/"
                )
                if (
                    not crawled_page
                    and vostfr_page >= CONFIG.FRENCH_ANIME_VOSTFR_LAST_PAGE
                ):
                    break

                vostfr_page += 1
            except Exception as e:
                break
            time.sleep(CONFIG.WAIT_BETWEEN_ALL)
