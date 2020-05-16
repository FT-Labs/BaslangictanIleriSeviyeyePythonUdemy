"""
Author : Arda
Date : 4/8/2020
"""


#Tuplelar

meyveler = ("elma" , "armut" , "portakal" )

#meyveler[0]  = "çilek"         //Tuplelarda eleman değişikliği yapılamaz, yeni eleman eklenemez.

meyveler1 = ("elma" , 3 )

#print(meyveler1)

meyveler2 = ("armut",)              # //Tuplelarda tek eleman girileceği zaman elemanın yanına virgül koyulması gerekmektedir.

#print(type(meyveler2))


isim = "Arda"
yas = 23

print( type((isim , yas)))