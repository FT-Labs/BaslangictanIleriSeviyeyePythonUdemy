"""
Author : Arda
Date : 4/29/2020
"""


kareListesi = [x**2 for x in range(1,6)]

kareGeneratoru = (x**2 for x in range(1,3))

for sayi in kareGeneratoru:
    print(sayi)

print(next(kareGeneratoru))



