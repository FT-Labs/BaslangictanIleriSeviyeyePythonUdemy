"""
Author : Arda
Date : 4/12/2020
"""


# kullaniciAdi = input("Kullanıcı adınızı giriniz.\n")      Girdi almaya yarar

#Kullanıcıdan 2 tane sayı talep edin, ilk büyüğü ve sonra küçüğü yazdırın.

# sayi1 = int(input("İlk sayıyı giriniz."))
# sayi2 = int(input("İkinci sayıyı giriniz."))

# if sayi1<sayi2:
#     kucukSayi = sayi1
#     buyukSayi = sayi2
# else:
#     kucukSayi = sayi2
#     buyukSayi = sayi1
#
# if  buyukSayi != kucukSayi:
#     print(f"""
#     Büyük Sayı : {buyukSayi}
#     Küçük Sayı : {kucukSayi}
#     """)
# else:
#     print("İki sayıda birbirine eşittir.")

sayilar = list()

for i in range(8):
    sayi = int(input(f"{i} numaralı sayıyı giriniz."))
    sayilar.append(sayi)

print(f"Girdiğiniz sayılar : {sayilar}")