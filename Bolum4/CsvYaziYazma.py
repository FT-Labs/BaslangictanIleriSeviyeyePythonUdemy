"""
Author : Arda
Date : 4/18/2020
"""

#EĞER TÜRKÇE BİLGİSAYAR KULLANIYORSANIZ SÜTUN ATLATMAK İÇİN
# ";" KULLANIN! "," KULLANIRSANIZ OLMAYACAKTIR!!

ogrenciler = ["Arda" , "Mehmet", "Ayşe" , "Caner" , "Güneş"]
notlar = [100 , 73 , 33 , 67 , 48]

#TÜRKÇE WİNDOWS KULLANIYORSANIZ dosya yazma okuma işlemlerinde 3.parametreye encoding="utf-8" YAZMAYI UNUTMAYINIZ!!


#İlk 2 sütunda (öğrenciler , notlar) yazacak
# with open("ogrenciler.csv" , "w") as dosyam:
#     dosyam.write("Öğrenciler , Notlar\n")
#
#     for sayi in range(len(ogrenciler)):
#         dosyam.write(f"{ogrenciler[sayi]},{notlar[sayi]}\n")


