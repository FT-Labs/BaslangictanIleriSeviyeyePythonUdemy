"""
Author : Arda
Date : 4/23/2020
"""

import random


bilgisayarPuani = 0
oyuncuPuani = 0

def TasKagitMakas(secim):
    rastgeleSayi = random.randint(0,2)
    tasKagitMakas = ["Taş" , "Kağıt" , "Makas"]

    bilgisayarSecimi = tasKagitMakas[rastgeleSayi]

    if secim == 'Kağıt':
        if bilgisayarSecimi == "Taş":
            print(f"Oyuncu Seçimi:{secim} , Bilgisayar Seçimi : {bilgisayarSecimi}\nOyuncu Kazandı!")
            return True
        elif bilgisayarSecimi == "Kağıt":
            print(f"Oyuncu Seçimi:{secim} , Bilgisayar Seçimi : {bilgisayarSecimi}\nBerabere!")
            return 3
        elif bilgisayarSecimi == "Makas":
            print(f"Oyuncu Seçimi:{secim} , Bilgisayar Seçimi : {bilgisayarSecimi}\nBilgisayar kazandı...")
            return False
    elif secim == "Taş":
        if bilgisayarSecimi == "Taş":
            print(f"Oyuncu Seçimi:{secim} , Bilgisayar Seçimi : {bilgisayarSecimi}\nBerabere!")
            return 3
        elif bilgisayarSecimi == "Kağıt":
            print(f"Oyuncu Seçimi:{secim} , Bilgisayar Seçimi : {bilgisayarSecimi}\nBilgisayar kazandı...")
            return False
        elif bilgisayarSecimi == "Makas":
            print(f"Oyuncu Seçimi:{secim} , Bilgisayar Seçimi : {bilgisayarSecimi}\nOyuncu Kazandı!")
            return True
    elif secim == "Makas":
        if bilgisayarSecimi == "Taş":
            print(f"Oyuncu Seçimi:{secim} , Bilgisayar Seçimi : {bilgisayarSecimi}\nBilgisayar kazandı...")
            return False
        elif bilgisayarSecimi == "Kağıt":
            print(f"Oyuncu Seçimi:{secim} , Bilgisayar Seçimi : {bilgisayarSecimi}\nOyuncu Kazandı!")
            return True
        elif bilgisayarSecimi == "Makas":
            print(f"Oyuncu Seçimi:{secim} , Bilgisayar Seçimi : {bilgisayarSecimi}\nBerabere!")
            return 3




while True:
    print("""
*****************************************
Taş Kağıt Makas Oyununa Hoş Geldiniz!
Oynamak için 1'e, çıkmak için 'q' ya basınız.
*****************************************
    """)

    girdi = input()

    if girdi == 'q':
        print("Oyundan çıkış yapılıyor...")
        break

    elif girdi == '1':
        secim = input("""Lütfen yapmak istediğiniz seçimi yazın.
Mevcut Seçimler : 'Taş' , 'Makas' , 'Kağıt' """)

        kazanan = TasKagitMakas(secim)

        if kazanan == 3:
            pass
        elif kazanan:
            oyuncuPuani += 1
        else:
            bilgisayarPuani += 1

        print(f"Oyun Durumu :\nBilgisayar : {bilgisayarPuani} Oyuncu : {oyuncuPuani}")
    else:
        print("Lütfen doğru bir seçim yapın.")
