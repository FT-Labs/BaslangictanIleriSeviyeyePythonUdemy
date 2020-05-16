"""
Author : Arda
Date : 5/8/2020
"""

from Bolum7MySQL.ImdbTop250DiziMYSQL.TopDiziler import TopDiziListesi
import mysql.connector as mysql

class VeriTabaniDiziler:
    def __init__(self):
        self.db = mysql.connect(user='arda' , passwd='12345678', host='localhost')
        self.cursor = self.db.cursor()
        self.cursor.execute("use top250dizi")

        self.cursor.execute("ALTER TABLE imdbDiziVerileri MODIFY yil VARCHAR(20)")
        self.db.commit()
        self.cursor.execute("ALTER TABLE imdbDiziVerileri MODIFY rating FLOAT(15,10)")
        self.db.commit()

    def veriTabaniSutunlariGoster(self):
        self.cursor.execute("DESC imdbDiziVerileri")
        print(self.cursor.fetchall())

    def DataBaseOlustur(self):
        self.cursor.execute("CREATE DATABASE top250dizi")
        self.cursor.execute("show databases")
        for dizi in self.cursor.fetchall():
            print(dizi)

    def TabloOlustur(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS imdbDiziVerileri (diziIsmi VARCHAR(200), yil VARCHAR (10), kadro VARCHAR(100), rating FLOAT(15,10),"
                            " oysayisi VARCHAR(20), link VARCHAR(200) )")

    def VerileriEkle(self):
        topDiziListesi = TopDiziListesi()
        diziListesi = topDiziListesi.dizileriOlustur()

        for dizi in diziListesi:
            for i in range(len(dizi)):
                dizi[i] = dizi[i].replace(",","")
                dizi[i] = dizi[i].replace("'", "")

            self.cursor.execute(f"INSERT INTO imdbDiziVerileri (diziIsmi,yil,kadro,rating,oysayisi,link) VALUES ('{dizi[0]}','{dizi[1]}','{dizi[2]}','{dizi[3]}','{dizi[4]}','{dizi[5]}')")
            self.db.commit()

    def VerileriSil(self):
        self.cursor.execute("DELETE FROM imdbDiziVerileri")
        self.db.commit()

    def VerileriGoster(self):
        self.cursor.execute("SELECT * FROM imdbDiziVerileri")
        for eleman in self.cursor.fetchall():
            print(eleman)

    def primaryKeyEkle(self):
        self.cursor.execute("ALTER TABLE imdbDiziVerileri ADD COLUMN siralama INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
        self.db.commit()

    def csvAktar(self):
        self.cursor.execute("SELECT * INTO OUTFILE 'top250diziler.csv' CHARACTER SET 'utf8' FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '\n' FROM imdbDiziVerileri")

veriTabaniDiziler = VeriTabaniDiziler()
veriTabaniDiziler.veriTabaniSutunlariGoster()
# veriTabaniDiziler.VerileriSil()
# veriTabaniDiziler.VerileriEkle()
# veriTabaniDiziler.primaryKeyEkle()
veriTabaniDiziler.VerileriGoster()
veriTabaniDiziler.csvAktar()



