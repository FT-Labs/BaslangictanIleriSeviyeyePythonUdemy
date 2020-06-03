"""
Author : Arda
Date : 4/19/2020
"""

#import Ogrenci
from Ogrenci import Ogrenci


# with open("öğrenciVize1.txt" , "r" , encoding="utf-8") as vize1Notlari:
#     ilkSatir = vize1Notlari.readline()
#
#     ayrilmisSatir = ilkSatir.split("->")
#
#     for eleman in range(len(ayrilmisSatir)):
#         ayrilmisSatir[eleman] = ayrilmisSatir[eleman].strip(" ")
#         ayrilmisSatir[eleman] = ayrilmisSatir[eleman].strip("\n")
#
#     print(ayrilmisSatir)

"""
Vize1 , Vize2 , Final notları dosya okuma ile okunacak.
Vize1 -> %30 , Vize2 -> %30 , Final -> %40 

AA->95-100 || BA->85-95 || BB->75-85 || CB->70-75 || CC->60-70 || DC->55-60 || DD-> 50-55 || FF(KALDI) -> 0-50
Not ortalamaları hesaplandıktan sonra csv dosyasına ilk sütun "isim", ikinci sütun "vize1", 
üçüncü sütun "vize2" , dördüncü sütun "final"
Sütunların altına notlar girilecek.
5.Sütuna "Harf Notu" yazılacak.
"""

class NotlariHesapla():
    def __init__(self , vize1DosyaAdi , vize2DosyaAdi , finalDosyaAdi):
        self.vize1DosyaAdi = vize1DosyaAdi
        self.vize2DosyaAdi = vize2DosyaAdi
        self.finalDosyaAdi = finalDosyaAdi
        self.ogrenciler = []


    def vize1Hesapla(self):

        with(open(self.vize1DosyaAdi , "r" , encoding="utf-8")) as vize1Notlari:

            vize1NotlariListesi = vize1Notlari.readlines()

            for satir in vize1NotlariListesi:
                satirListe = satir.split("->")
                for eleman in range(len(satirListe)):
                    satirListe[eleman] = satirListe[eleman].strip(" ")
                    satirListe[eleman] = satirListe[eleman].strip("\n")
                ogrenci = Ogrenci(satirListe[0] , int(satirListe[1]))
                self.ogrenciler.append(ogrenci)

    def vize2Hesapla(self):
        with(open(self.vize2DosyaAdi , "r" , encoding="utf-8")) as vize2Notlari:

            vize2NotlariListesi = vize2Notlari.readlines()

            for satir in vize2NotlariListesi:
                satirListe = satir.split("->")
                for eleman in range(len(satirListe)):
                    satirListe[eleman] = satirListe[eleman].strip(" ")
                    satirListe[eleman] = satirListe[eleman].strip("\n")
                for ogrenci in self.ogrenciler:
                    if satirListe[0] == ogrenci.isimSoyisim:
                        ogrenci.vize2 = int(satirListe[1])

    def finalHesapla(self):
        with(open(self.finalDosyaAdi , "r" , encoding="utf-8")) as finalNotlari:

            finalNotlariListesi = finalNotlari.readlines()

            for satir in finalNotlariListesi:
                satirListe = satir.split("->")
                for eleman in range(len(satirListe)):
                    satirListe[eleman] = satirListe[eleman].strip(" ")
                    satirListe[eleman] = satirListe[eleman].strip("\n")
                for ogrenci in self.ogrenciler:
                    if satirListe[0] == ogrenci.isimSoyisim:
                        ogrenci.final = int(satirListe[1])

    def harfNotuHesapla(self):
        #AA->95-100 || BA->85-95 || BB->75-85 || CB->70-75 || CC->60-70 || DC->55-60 || DD-> 50-55 || FF(KALDI) -> 0-50
        for ogrenci in self.ogrenciler:
            toplamPuan = ogrenci.vize1 * 0.3 + ogrenci.vize2 * 0.3 + ogrenci.final * 0.4
            if toplamPuan >= 95:
                ogrenci.harfNotu = "AA"
            elif toplamPuan < 95 and toplamPuan >=85:
                ogrenci.harfNotu = "BA"
            elif toplamPuan >=75 and toplamPuan <85:
                ogrenci.harfNotu = "BB"
            elif toplamPuan >= 70 and toplamPuan < 75:
                ogrenci.harfNotu = "CB"
            elif toplamPuan >=60 and toplamPuan < 70:
                ogrenci.harfNotu = "CC"
            elif toplamPuan >=55 and toplamPuan < 60:
                ogrenci.harfNotu = "DC"
            elif toplamPuan >= 50 and toplamPuan < 55:
                ogrenci.harfNotu = "DD"
            else:
                ogrenci.harfNotu = "KALDI"

    def csvOlustur(self):
        #TÜRKÇE BİLGİSAYAR KULLANIYORSANIZ BİR SONRAKİ SÜTUN İÇİN ";" YAZIN.
        #BEN İNGİLİZCE KULLANDIĞIMDAN ALTTAKİ KODDA "," İLE AYIRACAĞIM.
        with open("notlar.csv" , "w" ) as notlar:
            notlar.write("İsim Soyisim,Vize 1,Vize 2, Final, Harf Notu\n")

            for ogrenci in self.ogrenciler:
                notlar.write(f"{ogrenci.isimSoyisim},{ogrenci.vize1},{ogrenci.vize2},{ogrenci.final},{ogrenci.harfNotu}\n")





notlariHesapla = NotlariHesapla("öğrenciVize1.txt" , "öğrenciVize2.txt" , "öğrenciFinal.txt")
notlariHesapla.vize1Hesapla()
notlariHesapla.vize2Hesapla()
notlariHesapla.finalHesapla()
notlariHesapla.harfNotuHesapla()
notlariHesapla.csvOlustur()













