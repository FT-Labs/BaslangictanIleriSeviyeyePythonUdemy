"""
Author : Arda
Date : 4/15/2020
"""


def yuzuncuAsal():

    def AsalmiDegilmi(girdiSayi):
        if girdiSayi == 0 or girdiSayi == 1:
            return False
        elif girdiSayi == 2 or girdiSayi == 3:
            return True
        else:
            for bolen in range(2 , girdiSayi):
                if girdiSayi % bolen == 0:
                    return False
        return True

    sayi = 2
    sayac = 0

    while sayac < 100:
        if AsalmiDegilmi(sayi):
            sayac += 1

        sayi += 1

    return sayi-1

yuzuncuasal = yuzuncuAsal()

print(f"Yüzüncü Asal Sayı : {yuzuncuasal}")

