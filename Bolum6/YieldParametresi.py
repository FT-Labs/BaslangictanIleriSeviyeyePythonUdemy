"""
Author : Arda
Date : 4/29/2020
"""


def karesiniAl(sayilar):

    for sayi in sayilar:
        yield sayi**2



kareler = list(karesiniAl([1,2,3,5]))

print(kareler)
