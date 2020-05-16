"""
Author : Arda
Date : 4/15/2020
"""


# class Baslangic():
#     x = 5
#     y = 11.3
#
# baslangic = Baslangic()
#
# print(baslangic.x , baslangic.y)

# print(calisan1)
# print()
# print(calisan2)

# calisanListesi = [calisan1 , calisan2]
#
# for calisan in calisanListesi:
#     print(calisan)

class Calisan():
    def __init__(self , isim , soyisim , departman , maas):
        self.isim = isim
        self.soyisim = soyisim
        self.departman = departman
        self.maas = maas
    def __str__(self):
        return f"""
İsim : {self.isim}
Soyisim : {self.soyisim}
Departman : {self.departman}
Maaş : {self.maas}
        """
    def maasiArttir(self , arttirilacakMaas):
        self.maas += arttirilacakMaas
    def departmanDegistir(self , degistirilecekDepartman):
        self.departman = degistirilecekDepartman


calisan1 = Calisan("Mert" , "Akça" , "Bilgi İşlem" , 5500)
calisan2 = Calisan("Ayşe" , "Mutlu" , "İnsan Kaynakları" , 4500)

calisan2.maasiArttir(1000)
calisan1.departmanDegistir("Muhasebe")

print(calisan1)

