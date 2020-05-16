"""
Author : Arda
Date : 5/16/2020
"""

import smtplib
import mysql.connector as mysql
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailYolla:
    def __init__(self):
        self.kullanici_emaili = ""
        self.kullanici_sifre = ""
        self.mesaj = MIMEMultipart()
        self.mesaj_icerigi = ""

    def mesajOlustur(self , kime , konu , icerik):
        self.mesaj["From"] = self.kullanici_emaili
        self.mesaj["To"] = kime
        self.mesaj["Subject"] = konu
        self.mesaj_icerigi = icerik

    def emailYolla(self , adet):
        self.mesaj.attach(MIMEText(self.mesaj_icerigi , "plain"))
        try:
            smtp = smtplib.SMTP("smtp.gmail.com" , 587)
            smtp.starttls()
            smtp.login(self.kullanici_emaili , self.kullanici_sifre)
            text = self.mesaj.as_string()

            for i in range(adet):
                smtp.sendmail(self.kullanici_emaili , self.mesaj["To"], text)

            smtp.quit()
            return True
        except Exception as e:
            print(e)
            return False

class MySQLKullanicilar:
    def __init__(self):
        self.db = mysql.connect(user = 'arda' , passwd = '12345678' , database = 'email')
        self.cursor = self.db.cursor()

    def girisKontrolu(self , kullanici_adi , sifre):

        self.cursor.execute("SELECT * FROM kullanicilar")
        kullanicilar = self.cursor.fetchall()

        for kullanici in kullanicilar:
            if kullanici[0] == kullanici_adi and kullanici[1] == sifre:
                return True

        return False















