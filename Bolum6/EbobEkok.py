"""
Author : Arda
Date : 4/23/2020
"""


# EBOB NE?
# EBOB verilen sayılar içerisindeki en büyük ortak bölendir.   (18 , 24 , 30) -> EBOB = 6

class EBOBEKOK:
    def __init__(self, sayilar):
        self.sayilar = sayilar

    def EbobBul(self):
        self.sayilar.sort()

        ebob = 0
        for bolen in range(1 , self.sayilar[0] + 1):
            bolenListesi = [sayi % bolen == 0 for sayi in self.sayilar]

            if all(bolenListesi):
                ebob = bolen

        print(f"Bu sayıların EBOB'u : {ebob}")


    def EkokBul(self):

        ekok = 1
        self.sayilar.sort()

        bolenListesi = self.sayilar
        enBuyukSayi = self.sayilar[-1]
        bolen = 2

        while not all([sayi == 1.0 for sayi in bolenListesi]):
            bolunenVarmi = [sayi % bolen == 0 for sayi in bolenListesi]
            bolenListesi = [sayi / bolen if sayi % bolen == 0 else sayi for sayi in self.sayilar]
            self.sayilar = bolenListesi

            if any(bolunenVarmi):
                ekok *= bolen

            bolen += 1

            if bolen > enBuyukSayi:
                bolen = 2

        print(f"Bu Sayıları En Küçük Bölen İlk Sayı : {ekok}")



sayiListesi = [6 ,  12 , 24 , 96 , 120]
eboblar = EBOBEKOK(sayiListesi)
eboblar.EkokBul()



