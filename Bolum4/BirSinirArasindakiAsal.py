"""
Author : Arda
Date : 4/13/2020
"""

sinir = int(input("Asal sayıların bulunmasını istediğiniz sınırı girin."))


def asallariBul(sinir):
    asallar = []

    for sayi in range(sinir):
        if sayi == 2:
            asallar.append(sayi)
        elif sayi == 3:
            asallar.append(sayi)
        else:
            for bolen in range(2 , sayi):
                if sayi%bolen == 0:
                    break
                else:
                    if bolen + 1 == sayi:
                        asallar.append(sayi)
    return asallar


asalListesi = asallariBul(sinir)

print(f"{sinir} içindeki asal sayılar : {asalListesi}")








