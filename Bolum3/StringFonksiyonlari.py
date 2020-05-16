"""
Author : Arda
Date : 4/11/2020
"""

# print(len(isim))      len() Fonksiyonu objenin uzunluğunu alır.


# print(isim.upper())    upper() Fonksiyonu karakterleri büyük hale getirir.
# print(isim.capitalize())   capitelizer() Fonksiyonu ilk karakteri büyük hale çevirir.

# isim1 = ";Gülşah;"        strip() Fonksiyonu içine girilen string'e bağlı olarak sağdan yada soldan kısaltır.
# print(isim1.strip(";"))   Sağ için -> rstrip()    Sol için -> lstrip()

# print(isim.replace("a" , "B"))    replace() komutu verilen iki string'i birbiriyle değiştirir.

isim = "Alp"
yas = "25"
semt = "Ataşehir"

# print("Benim adım {}, yaşım {} , {}'de oturuyorum.".format(isim , yas , semt))
# print("Yaşım {1} ,{2}'de oturuyorum ve ismim {0}.".format(isim , yas ,semt))

# F-Stringler , yazımı -> f""

print(f"Benim adım {isim}, yaşım {yas}, {semt}'te oturuyorum.")