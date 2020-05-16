"""
Author : Arda
Date : 4/13/2020
"""


while True:
    try:
        sayi1 = int(input("İlk sayıyı giriniz."))
        sayi2 = int(input("İkinci sayıyı giriniz."))
        islem = input("Lütfen yapılmasını istediğiniz işlemi giriniz.\nGeçerli İşlemler : (+ , - , * , /)\nÇıkış Yapmak İçin 'q'ya Basınız.")

        if islem == "+":
            print(f"Sayıların Toplamı : {sayi1 + sayi2}")
        elif islem == "-":
            print(f"Sayıların Farkı : {sayi1 - sayi2}")
        elif islem == "/":
            print(f"Sayıların Bölümü : {sayi1 / sayi2}")
        elif islem == "*":
            print(f"Sayıların Çarpımı : {sayi1 * sayi2}")
        elif islem == 'q':
           break
        else:
            print("Lütfen geçerli bir işlem girin.")
    except:
        print("Lütfen doğru bir sayı girin.")


