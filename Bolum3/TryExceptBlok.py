"""
Author : Arda
Date : 4/12/2020
"""


# try:
#     sayi = int(input("Sayıyı giriniz."))
# except Exception as e:
#     raise e
# finally:
#     print("Blok sonlandırılmıştır.")

# sayi = int(input("Lütfen pozitif bir sayı girin."))
# if sayi<0:
#     raise Exception("Girdiğiniz sayı pozitif değil.")

try:
    sayi1 = int(input("İlk sayıyı giriniz."))
    sayi2 = int(input("İkinci sayıyı giriniz."))
except Exception as e:
    print(Exception("Lütfen sayıları doğru girin."))
    raise e

if sayi1<sayi2:
    kucukSayi = sayi1
    buyukSayi = sayi2
else:
    kucukSayi = sayi2
    buyukSayi = sayi1

if  buyukSayi != kucukSayi:
    print(f"""
    Büyük Sayı : {buyukSayi}
    Küçük Sayı : {kucukSayi}
    """)
else:
    print("İki sayıda birbirine eşittir.")

