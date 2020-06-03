"""
Author : Arda
Date : 4/21/2020
"""

from Oyuncu import *
import random

# damien = Oyuncu("Damien" , "İnsan" , 100 , Silah())
# ogre = Yaratik("Ogre" , 3 , 40)
# print(damien)
# for sayi in range(70):
#     ogre.hasarAl(damien.hasarVer())
# damien.silah = kilic
#
# vampir = Vampir()
#
# for oyunTuru in range(50):
#     vampir.hasarAl(damien.hasarVer())

damien = KilicUstasi("Damien")
tabanca = Silah("Tabanca" , hasar = 6)
kilic = Silah("Kılıç" , 9)

christie = Silahsor("Christie")
christie.silah = tabanca

KinggOgre = KralOgre("King Ogre!!!")

for oyunTuru in range(100):
    KinggOgre.hasarAl(christie.hasarVer())







