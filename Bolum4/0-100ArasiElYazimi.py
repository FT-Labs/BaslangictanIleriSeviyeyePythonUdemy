"""
Author : Arda
Date : 4/14/2020
"""


def ElYazimi(sayi):
    birler = {0 : "Sıfır" , 1 : "Bir" , 2 : "İki" , 3 : "Üç" , 4 : "Dört" ,
              5 : "Beş" , 6 : "Altı" , 7 : "Yedi" , 8 : "Sekiz" , 9 : "Dokuz"}

    onlar = {1 : "On" , 2 : "Yirmi" , 3 : "Otuz" , 4 : "Kırk" ,
             5 : "Elli" , 6 : "Altmış" , 7 : "Yetmiş" , 8 : "Seksen" , 9 : "Doksan" , 10 : "Yüz"}


    if sayi//10 == 0:
        return f"{birler[sayi]}"
    else:
        sayiString = str(sayi)
        birlerBasamagi = int(sayiString[1])
        onlarBasamagi = sayi // 10

        if sayi%10 != 0:
            return f"{onlar[onlarBasamagi]}{str(birler[birlerBasamagi]).lower()}"
        else:
            return f"{onlar[onlarBasamagi]}"



while True:
    try:
        girdi = input("El ile yazılması istenen sayıyı giriniz, lütfen 0-100 aralığında olsun.\nÇıkış için 'q' ya basın.\n")

        if girdi == "q":
            break
        else:
            intGirdi = int(girdi)
            elYazimi = ElYazimi(intGirdi)
            print(elYazimi)
    except Exception as e:
        print("Hatalı işlem yaptınız, işlem hatası : {}".format(e))

