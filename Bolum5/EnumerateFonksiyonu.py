"""
Author : Arda
Date : 4/24/2020
"""

sebzeler = ["Brokoli" , "Atom" , "Biber" , "Salatalık" , "Maydonoz" , "Patlıcan" , "Karnıbahar"]


# for sayi in range(len(sebzeler)):             Zor Yol!!
#     print(f"{sayi} : {sebzeler[sayi]}")


#enumerate()    Listenin elemanlarını indeksler.

for sayi,sebze in enumerate(sebzeler):
    print(f"{sayi+1} : {sebze}")
