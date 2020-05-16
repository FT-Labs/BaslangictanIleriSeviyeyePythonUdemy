"""
Author : Arda
Date : 4/26/2020
"""

import random


"""
YÖNERGELER : Bu projede mastermind oyununu yazacağız, bilmiyorsanız google'dan biraz bakmanız sizin için iyi olur.

Öncelikle bu oyunu bilgisayara karşı oynayacağız. Bilgisayar bize 4 tane harften oluşacak rastgele bir
string üretecek, ismide secret(sır) olacak ve bunu secretOlustur fonksiyonu ile oluşturacak. 
"A , B , C , D , E , F " den oluşacak, ve aynı harfi birden fazla kez kullanabilir olacak.

Bizde bilgisayarın bu oluşturduğu random string'i tahmin etmeye çalışacağız. Program bizim yazdığımız string'e
göre bize iki paremetre dönecek, bu paramatreler bir classın içinde yer alacak.

İlk parametre -> dogruYer : Bilgisayar kendi oluşturduğu stringi ve bizimkini kıyaslayacak. Eğer iki stringinde herhangi
bir elemanı aynı ise dogruYer parametresine 1 eklenecek.

ÖRNEK : Secret = "ABDD" -> Tahminimiz = "ACDB"
                    dogruYer = 2
                    yanlisYer = 1

İkinci parametre -> yanlisYer : Bu parametre ise secret'ta mevcut bulunan bir elemanın bizim tahminimizde yer alması, fakat
yerinin yanlış olması olacak. Bu durumda yanlisYer parametresine 1 eklenecek.

ÖRNEK : Secret = "ACBB" -> Tahminimiz = "BBDD" 
                    yanlisYer = 2
                    dogruYer = 0
                    
Eğer bilgisayar bize dogruYer = 4 ve yanlisYer = 0 dönerse kullanıcı oyunu kazanacak.
"""


class Tahmin:
    def __init__(self , dogruYer , yanlisYer):
        self.dogruYer = dogruYer
        self.yanlisYer = yanlisYer


class Mastermind:
    def __init__(self):
        self.secret = ""
        self.oyuncuSecret = ""

        self.secretOlustur()

    def secretOlustur(self):
        elemanListesi = ["A", "B", "C", "D", "E", "F"]

        for _ in range(4):
            rastgeleSayi = random.randint(0, 5)
            self.secret += elemanListesi[rastgeleSayi]

    def oyunuOyna(self):

        while True:

            try:
                self.oyuncuSecret = input("Lütfen tahmininizi girin. Tahmin 4 Harften oluşsun, ve içereceği harfler:\n'A,B,C,D,E,F'\n")
                dogruYerCikartilmisSecret, dogruYerCikartilmisOyuncuSecret, dogruYer = self.dogruYerHesapla()
                yanlisYer = self.yanlisYerHesapla(dogruYerCikartilmisOyuncuSecret , dogruYerCikartilmisSecret)

                tahmin = Tahmin(dogruYer , yanlisYer)

                if tahmin.dogruYer == 4 and tahmin.yanlisYer == 0:
                    print("Tebrik Ederim! Oyunu kazandınız, tahmininiz doğru.")
                    break
                else:
                    print(f"Tahmininiz maalesef yanlış.\nDoğru Yer : {tahmin.dogruYer} , Yanlış Yer : {tahmin.yanlisYer} ")

            except:
                print("Lütfen sırınızı doğru girin.")

    def dogruYerHesapla(self):

        dogruYer = 0
        dogruYerlerinListesi = []

        for sayi in range(len(self.secret)):
            if self.secret[sayi] == self.oyuncuSecret[sayi]:
                dogruYer += 1
                dogruYerlerinListesi.append(sayi)

        dogruYerCikartilmisSecret = ""
        dogruYerCikartilmisOyuncuSecret = ""

        for sayi in range(4):
            if not dogruYerlerinListesi.__contains__(sayi):
                dogruYerCikartilmisSecret += self.secret[sayi]
                dogruYerCikartilmisOyuncuSecret += self.oyuncuSecret[sayi]

        return dogruYerCikartilmisSecret , dogruYerCikartilmisOyuncuSecret , dogruYer

    def yanlisYerHesapla(self , dogruYerCikartilmisOyuncuSecret , dogruYerCikartilmisSecret):

        oyuncuSecretSozluk = {"A" : 0 , "B" : 0 , "C" : 0 , "D" : 0 , "E" : 0 , "F" : 0}
        secretSozluk = oyuncuSecretSozluk.copy()

        for karakter in dogruYerCikartilmisSecret:
            if karakter in secretSozluk.keys():
                secretSozluk[karakter] += 1

        for karakter in dogruYerCikartilmisOyuncuSecret:
            if karakter in oyuncuSecretSozluk.keys():
                oyuncuSecretSozluk[karakter] += 1

        yanlisYer = 0

        for key in oyuncuSecretSozluk.keys():
            yanlisYer += min(oyuncuSecretSozluk[key] , secretSozluk[key])

        return yanlisYer



if __name__ == "__main__":

    print("""
*****************************
Mastermind Oyununa Hoşgeldiniz!
*****************************
""")

    oyun = Mastermind()
    oyun.oyunuOyna()













