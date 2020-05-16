"""
Author : Arda
Date : 4/20/2020
"""


#Kalıtım (Inheritance) -> bir üst class'ın özelliklerini kendine alır.

class Insan():
    def __init__(self , isim , soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def isimSoyisimYazdir(self):
        print(self.isim , self.soyisim)


class Ogrenci(Insan):
    def __init__(self , isim , soyisim , mezuniyetYili):
        #Insan.__init__(self , isim , soyisim)  1.yol
        super().__init__(isim , soyisim)   #2.yol
        self.mezuniyetYili = mezuniyetYili

    def isimSoyisimYazdir(self):
        super(Ogrenci, self).isimSoyisimYazdir()
        print(f"Mezuniyet Yılı : {self.mezuniyetYili}")



ogrenci1 = Ogrenci("Mehmet" , "Aydoğan" , 2018)
ogrenci1.isimSoyisimYazdir()