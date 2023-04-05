import logging

from toroplay import Toroplay

film_data = {
    "title": "My Hero Academia",
    "description": "Izuku Midoriya rêve de rejoindre la filière super-héroïque du grand lycée Yūei et de devenir un jour un des plus grands héros.",
    "post_type": "series",
    "trailer_id": "",
    "fondo_player": "https://french-anime.com/images/french-anime-4c58-c9cf-00f9-4d71.jpg",
    "poster_url": "https://french-anime.com/images/french-anime-4c58-c9cf-00f9-4d71.jpg",
    "extra_info": {
        "titre original": "Boku no Hero Academia ",
        "date de sortie": "2022 ",
        "genre": " Animes VF, Action, Comédie ",
        "acteurs": "Daiki Yamashita, Nobuhiko Okamoto, Kenta Miyake, Yûki Kaji",
        "version": "FRENCH",
        "durée": "1h 24 mn",
        "synopsis": "Izuku Midoriya rêve de rejoindre la filière super-héroïque du grand lycée Yūei et de devenir un jour un des plus grands héros.",
    },
}

season_str = "Saison 06 FRENCH"

film_links = {
    "1": [
        "https://uqload.co/embed-y6hp7w62a5s0.html",
        "https://vudeo.net/embed-ise0412bhx89.html",
        "https://upstream.to/embed-v4wiaphzqbn3.html",
        "https://doodstream.com/e/8vbbljz63zm1",
    ],
    "2": [
        "https://uqload.co/embed-zl1koxtkcvy9.html",
        "https://vudeo.net/embed-oftic4m927ai.html",
        "https://upstream.to/embed-7twduuo20a4z.html",
        "https://doodstream.com/e/krw32mikkvo8",
    ],
    # "3": [
    #     "https://uqload.co/embed-yz223oipv5f8.html",
    #     "https://vudeo.net/embed-9gr3et4jtmb8.html",
    #     "https://upstream.to/embed-anrfim65l5rj.html",
    #     "https://doodstream.com/e/xh65eupzy91j",
    # ],
    # "4": [
    #     "https://uqload.co/embed-0g1lo0xpq4ye.html",
    #     "https://vudeo.net/embed-z09o52tk4inf.html",
    #     "https://upstream.to/embed-ubydg5kgxft9.html",
    #     "https://doodstream.com/e/r4pc3b8n2eve",
    # ],
    # "5": [
    #     "https://uqload.co/embed-rhn6jf724bht.html",
    #     "https://vudeo.net/embed-4uyclxh14hni.html",
    #     "https://upstream.to/embed-s7vutliqlr34.html",
    #     "https://doodstream.com/e/spuhn9fr54f5",
    # ],
    # "6": [
    #     "https://uqload.co/embed-ch3zej7z88e3.html",
    #     "https://vudeo.net/embed-1rsr6hyws46s.html",
    #     "https://upstream.to/embed-um0ra6t1hib9.html",
    #     "https://doodstream.com/e/4saceiecmo1y",
    # ],
    # "7": [
    #     "https://uqload.co/embed-xp89zc48octa.html",
    #     "https://vudeo.net/embed-bl43ie6xmkln.html",
    #     "https://upstream.to/embed-f7d75o6cujon.html",
    #     "https://doodstream.com/e/r4jjqtb2z68b",
    # ],
    # "8": [
    #     "https://uqload.co/embed-xn6ujp5bf1bb.html",
    #     "https://vudeo.net/embed-t8v3fn7x5dmo.html",
    #     "https://upstream.to/embed-6uelhacwevj1.html",
    #     "https://doodstream.com/e/tsdh9ezw6i59",
    # ],
    # "9": [
    #     "https://uqload.co/embed-6t5y5fdyp9vh.html",
    #     "https://vudeo.net/embed-i38m3ut36wmo.html",
    #     "https://upstream.to/embed-abnrmj51jf8z.html",
    #     "https://doodstream.com/e/xtrcguf9c9b2",
    # ],
    # "10": [
    #     "https://uqload.co/embed-hl1d3jzvmi5q.html",
    #     "https://vudeo.net/embed-ngx7i1gwf2w9.html",
    #     "https://upstream.to/embed-y7k3rxnkp6d9.html",
    #     "https://doodstream.com/e/uscc77982ao3",
    # ],
    # "11": [
    #     "https://uqload.co/embed-4o9pp37qxhy4.html",
    #     "https://vudeo.net/embed-iui1l3d85stg.html",
    #     "https://upstream.to/embed-4u5m473i7yln.html",
    #     "https://doodstream.com/e/vvlyoggdg68b",
    # ],
    # "12": [
    #     "https://uqload.co/embed-yed644yyo29r.html",
    #     "https://vudeo.net/embed-7b32aarxudb5.html",
    #     "https://upstream.to/embed-47f6l0emuaa.html",
    #     "https://doodstream.com/e/jaeklgt4d6ts",
    # ],
    # "13": [
    #     "https://uqload.co/embed-mme6n6jqtnn1.html",
    #     "https://vudeo.net/embed-b7sjslvurg4f.html",
    #     "https://upstream.to/embed-fsl758flreln.html",
    #     "https://doodstream.com/e/f1ltn8hxsyao",
    # ],
    # "14": [
    #     "https://uqload.co/embed-ngtxm67fw4rr.html",
    #     "https://vudeo.net/embed-j6zbs3zfcuh.html",
    #     "https://upstream.to/embed-mg4l141ff9pc.html",
    #     "https://doodstream.com/e/rn1vb6w4ycxk",
    # ],
    # "15": [
    #     "https://sbhight.com/e/itswd4h2ybn5.html",
    #     "https://vudeo.net/embed-pjkp3wt57ow0.html",
    #     "https://upstream.to/embed-3isqv53bxgvi.html",
    #     "https://doodstream.com/e/cezk45chaze5",
    # ],
    # "16": [
    #     "https://uqload.co/embed-ebenq3d0zv04.html",
    #     "https://vudeo.net/embed-vkuq9l5hr9h6.html",
    #     "https://upstream.to/embed-02d9ru4ll1vr.html",
    #     "https://doodstream.com/e/ucmzebx9s7py",
    # ],
    # "17": [
    #     "https://uqload.co/embed-lbpcczujpixk.html",
    #     "https://vudeo.net/embed-r0mfkqcpv18q.html",
    #     "https://streamhide.to/e/q110vg7r6p4t",
    #     "https://doodstream.com/e/kyag3hbagz0j",
    # ],
    # "18": [
    #     "https://uqload.co/embed-oecv2e4qe6h7.html",
    #     "https://vudeo.net/embed-asjarq36p5j6.html",
    #     "https://sbbrisk.com/e/p73w6s3enep1.html",
    #     "https://doodstream.com/e/j2u605e2vb1o",
    # ],
    # "19": [
    #     "https://uqload.co/embed-tia9p8kyoixn.html",
    #     "https://vudeo.net/embed-mcg7b1k877ym.html",
    #     "https://upstream.to/embed-qmdr7thpsycn.html",
    #     "https://doodstream.com/e/20y2xsv3yoy9",
    # ],
    # "20": [
    #     "https://uqload.co/embed-nwcs8z8rtiit.html",
    #     "https://vudeo.net/embed-6piibf70xho8.html",
    #     "https://streamhide.to/e/2wobebfy0zgx",
    #     "https://doodstream.com/e/7j09w3epu4pc",
    # ],
    # "21": [
    #     "https://uqload.co/embed-p8vc6s5aqalb.html",
    #     "https://vudeo.net/embed-3wmdc9l9qt2r.html",
    #     "https://streamhide.to/e/0bd8qpziza5v",
    #     "https://doodstream.com/e/sy6isqo40kad",
    # ],
    # "22": [
    #     "https://uqload.co/embed-trg7yydri6uv.html",
    #     "https://vudeo.net/embed-ix7ap5izpd1h.html",
    #     "https://streamhide.to/e/q2ryaazrh8j7",
    #     "https://doodstream.com/e/3u4s6ruj0wh0",
    # ],
    # "23": [
    #     "https://uqload.co/embed-xua9mvtnuo7f.html",
    #     "https://vudeo.net/embed-g33rbt7hhii5.html",
    #     "https://streamhide.to/e/p8sdp96n2vp8",
    #     "https://doodstream.com/e/4kv4otkm9v6q",
    # ],
}

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)


def main():
    Toroplay(film_data, film_links, season_str=season_str).insert_film()


if __name__ == "__main__":
    main()
