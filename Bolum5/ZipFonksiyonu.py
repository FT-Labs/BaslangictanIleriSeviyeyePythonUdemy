"""
Author : Arda
Date : 4/24/2020
"""

#zip() İki farklı iterasyon yapılabilen öğeyi alır, ve elemanları birbirine bağlar.

# a = [1,2]
# b = [3,4]
# for x in zip(a,b):
#     print(x)

# İki tane string alsın. Bu iki stringin içindeki sırası ve konumu aynı olan elemanları bastırsın.

a = "Merhabalar"
b = "Mrrhblalrr"

for elemanlar in zip(a ,b):

    if elemanlar[0] == elemanlar[1]:
        print(elemanlar[0])

