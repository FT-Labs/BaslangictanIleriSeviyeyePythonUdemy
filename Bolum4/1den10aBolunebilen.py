"""
Author : Arda
Date : 4/13/2020
"""


sayi = 11

def tamBolen(x):
    for bolen in range(1 , 11):
        if sayi%bolen == 0:
            continue
        else:
            return False
    return True

bolen = True

while bolen:
    if not tamBolen(sayi):
        sayi += 1
    else:
        print(f"1den 10a kadar sayılara bölünebilen ilk tamsayı : {sayi}")
        bolen = False







