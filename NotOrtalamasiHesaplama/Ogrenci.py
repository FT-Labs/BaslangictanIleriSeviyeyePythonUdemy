"""
Author : Arda
Date : 4/19/2020
"""


class Ogrenci():
    def __init__(self , isimSoyisim , vize1 = 0 , vize2 = 0 , final = 0 , harfNotu = ""):
        self.isimSoyisim = isimSoyisim
        self.vize1 = vize1
        self.vize2 = vize2
        self.final = final
        self.harfNotu = harfNotu
    def __str__(self):
        return self.isimSoyisim
