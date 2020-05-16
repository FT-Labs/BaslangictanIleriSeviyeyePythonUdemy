"""
Author : Arda
Date : 4/14/2020
"""

sinir = int(input("Asal sayıların bulunmasını istediğiniz aralığı girin."))


def asallariBul(sinir):

    def asalMiDegilmi(x):
        if x == 0 or x == 1:
            return False
        for bolen in range(2, x):
            if x % bolen == 0:
                return False
        return True

    asallar = list()

    for sayi in range(sinir):
        if sayi == 2:
            asallar.append(sayi)
        elif sayi == 3:
            asallar.append(sayi)
        else:
            if asalMiDegilmi(sayi):
                asallar.append(sayi)

    return asallar

asalListesi = asallariBul(sinir)

print(f"{sinir} içerisindeki asallar : {asalListesi}")