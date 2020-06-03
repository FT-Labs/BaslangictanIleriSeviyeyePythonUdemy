"""
Author : Arda
Date : 4/21/2020
"""

import sys
import random

class Silah:
    def __init__(self , isim = "Yumruk" , hasar = 3):
        self.isim = isim
        self.hasar = hasar

class Oyuncu:
    def __init__(self , isim , irk , yasamPuani , silah):
        self.isim = isim
        self.irk = irk
        self.yasamPuani = yasamPuani
        self.silah = Silah()

    def hasarVer(self):
        return self.silah.hasar

    def __str__(self):
        return f"""
İsim = {self.isim}
Irk = {self.irk}
Yaşam Puanı = {self.yasamPuani}
Silah = {self.silah.isim} , Hasar = {self.silah.hasar}
"""

class KilicUstasi(Oyuncu):
    def __init__(self , isim , irk = "Kılıç Ustası" , yasamPuani = 150 , silah = Silah()):
        #Oyuncu.__init__(self ,isim , irk , yasamPuani , silah)   1.yol
        super().__init__(isim , irk , yasamPuani , silah)     #2.yol

    def hasarVer(self):
        if self.silah.isim == "Kılıç":
            print("Kılıç Ustası özel silahını kullandığından 2 kat hasar veriyor! Hasar : {}".format(self.silah.hasar * 2))
            return self.silah.hasar * 2

        return self.silah.hasar

class Silahsor(Oyuncu):
    def __init__(self , isim , irk = "Silahşör" , yasamPuani =75 , silah  = Silah()):
        super().__init__(isim , irk , yasamPuani , silah)

    def hasarVer(self):
        #Yüzde 10 olasılıkla silahşör kafadan vuruş yapıp 4 kat hasar verir!
        if self.silah.isim == "Tabanca":
            rastgele = random.randint(1,10)
            if rastgele != 1:
                print("Silahşör özel silahını kullandığından 2 kat hasar veriyor!")
                return self.silah.hasar * 2
            else:
                print("Silahşör kafadan vuruş yaparak 4 kat hasar verdi!")
                return self.silah.hasar * 4

        return self.silah.hasar




class Yaratik:
    def __init__(self , isim , can , yasamPuani):
        self.isim = isim
        self.can = can
        self.yasamPuani = yasamPuani
        self.yasamPuaniYenile = self.yasamPuani

    def hasarAl(self , hasar):

        if self.yasamPuani <= 0:
            self.can -= 1
            if self.can < 0:
                print(f"{self.isim} başarıyla öldürdünüz.")
                sys.exit()
            else:
                print(f"{self.isim} ' in {self.can} canı kaldı.")
                self.yasamPuani = self.yasamPuaniYenile

        self.yasamPuani -= hasar
        print(f"{self.isim} {hasar} hasar aldı!\nKalan Yaşam Puanı : {self.yasamPuani} , Kalan Can : {self.can}")


class Vampir(Yaratik):
    def __init__(self , isim = "Vampir" , can = 5 , yasamPuani = 23):
        super().__init__(isim , can , yasamPuani)

    def hasarAl(self , hasar):
        print("Vampir özel gücünden dolayı yarı hasar alıyor!")
        super().hasarAl(hasar / 2)

class Ogre(Yaratik):
    def __init__(self , isim = "Ogre" , can = 2 , yasamPuani = 110):
        super().__init__(isim , can , yasamPuani)

class KralOgre(Ogre):
    def __init__(self , isim , can = 3, yasamPuani = 160):
        super().__init__(isim , can , yasamPuani)

    def hasarAl(self , hasar):
        #Kral ogrenin yüzde 25 şans ile hasarı savuşturma ihtimali vardır!
        rastgele = random.randint(1,4)
        if rastgele == 1:
            print("Kral Ogre saldırınızı savuşturmayı başardı!")
            super().hasarAl(0)
        else:
            super().hasarAl(hasar)


















