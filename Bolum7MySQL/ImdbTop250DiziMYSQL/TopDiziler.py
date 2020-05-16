"""
Author : Arda
Date : 5/8/2020
"""

import requests
from bs4 import BeautifulSoup


class TopDiziListesi:

    def dizileriOlustur(self):
        url = "https://www.imdb.com/chart/toptv/"
        cevap = requests.get(url)

        soup = BeautifulSoup(cevap.text , "lxml")

        diziler = soup.select('td.titleColumn')
        linkler = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        linkler = [f"https://www.imdb.com{link}" for link in linkler]
        aktorler = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        rating = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        oylar = [b.attrs.get('title') for b in soup.select('td.ratingColumn strong')]
        oylar = [oy.split(" ")[3] for oy in oylar]

        top250dizi = list()

        for girdi in range(len(diziler)):

            dizi_string = diziler[girdi].get_text()
            dizi = (" ".join(dizi_string.split()).replace('.' , ','))
            dizi_ismi = dizi[len(str(girdi)) + 1 : -7]
            yil = dizi[-7:].strip(" ")
            yil = yil.strip("(")
            yil = yil.strip(")")

            dizi_bilgileri = [dizi_ismi,
                               yil,
                               aktorler[girdi],
                               rating[girdi],
                               oylar[girdi],
                               linkler[girdi]]

            top250dizi.append(dizi_bilgileri)

        return top250dizi
