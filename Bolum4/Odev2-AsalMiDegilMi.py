"""
Author : Arda
Date : 4/15/2020
"""



def AsalMiDegilMi(sayi):
    if sayi == 2 or sayi == 3:
        return True
    elif sayi == 1 or sayi == 0:
        return False
    else:
        for bolen in range(2 , sayi):
            if sayi % bolen == 0:
                return False

    return True


while True:
    try:
        sayi = input("Asal olup olmadığına bakılmak istenen sayıyı giriniz.\nÇıkış için 'q' ya basınız.")

        if sayi == 'q':
            break
        else:
            if int(sayi)<0:
                raise Exception("Lütfen 0'dan büyük bir sayı girin. Negatif sayılar asal sayı olarak değerlendirilmez.")
            if AsalMiDegilMi(int(sayi)):
                print(f"{sayi} bir asal sayıdır.")
            else:
                print(f"{sayi} bir asal sayı değildir.")
    except Exception as e:
        print(f"Lütfen geçerli bir sayı girin.\n Hata Kodu : {e}")
