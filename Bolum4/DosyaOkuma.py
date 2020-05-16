"""
Author : Arda
Date : 4/18/2020
"""

# read için "r" komutu kullanılır.
#.read(sayı) Buradaki sayı toplam okunacak karakter sayısını gösterir.
#.readline() komutu tek bir satırı okur.
#.readlines() satırların her birini liste oluşturup ekler.
#.tell() dosyada hangi karakterde olduğunuzu döner.

# with open("ucuncudosyam.txt" , "w+" , encoding="utf-8") as dosyam:
#     print(dosyam.readline())
#     print(dosyam.tell())
#     dosyam.write("asddas")
#     print(dosyam.read())

with open("dorduncudosyam.txt" , "r+" , encoding="utf-8") as dosyam:
    print(dosyam.read())
    dosyam.write("r+ komutu yeniden.")





