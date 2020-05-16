"""
Author : Arda
Date : 4/25/2020
"""


sayilar = [1 , 3 , 5 ,7]
meyveler = ["portakal" , "elma" , "armut" , "çilek"]
sayilar1 = [2 , 1 , 3 , 1]


# print(list(map(lambda x : x+x , sayilar)))


print(dict(map(lambda x , y : (x , y) , meyveler , sayilar1)))