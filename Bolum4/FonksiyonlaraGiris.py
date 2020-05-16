"""
Author : Arda
Date : 4/12/2020
"""


# sayi1 = 13
# sayi2 = 155

# def sayilariTopla(sayi1 , sayi2):
#     print("Sayılar toplanıyor...")
#     return sayi1+sayi2
#
#
# toplam = sayilariTopla(sayi1 , sayi2)
# print(toplam)

# def sayilariTopla(x , y , z):
#     return x+y+z
#
# sayi1 = int(input("İlk sayıyı girin."))
# sayi2 = int(input("İkinci sayıyı girin."))
# sayi3 = int(input("Üçüncü sayıyı girin."))
#
# toplam = sayilariTopla(sayi1 , sayi2 , sayi3)
#
# print(f"Sayıların toplamı = {toplam}")


# kullaniciAdi = input("Lütfen kullanıcı adınızı girin.")
#
# def merhabaKullanici(kullaniciAdi):
#     print(f"Merhaba, kullanıcı adınız : {kullaniciAdi}")
#
# merhabaKullanici(kullaniciAdi)

# isim = input("İsminizi girin.")
# soyIsim = input("Soy adınızı girin.")
#
# def isimSozluk(isim , soyIsim):
#     return {"İsim" : isim , "Soy Ad" : soyIsim}
#
# sozluk = isimSozluk(isim , soyIsim)
#
# print(sozluk)

sayi = int(input("Lütfen sayıyı girin."))

def listeSayilar(sayi):
    sayiListesi = list()
    for sayi in range(sayi):
        sayiListesi.append(sayi)
    return sayiListesi

liste = listeSayilar(sayi)

print(liste)



