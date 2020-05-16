"""
Author : Arda
Date : 4/25/2020
"""

sayiListesi = [1, 2 , 4 , 5 , 8 , 10 , 11 , 13 , 14 , 16]

def ikiyeBol(x):
    if x%2==0:
        return x


# for sayi in filter(lambda x : x if x%2 == 0 else None , sayiListesi ):
#     print(sayi)

# for sayi in filter(ikiyeBol, sayiListesi ):
#     print(sayi)

isim = "aBaaaaaCaaMaaNa"

# for eleman in filter(lambda x : True if x=="a" else None , isim):
#     print(eleman)

ikiyeBolunenler = list(filter(lambda x : x if x%2==0 else None , sayiListesi))


a = [1,2]
b = [3,4]

print(list(zip(a,b)))