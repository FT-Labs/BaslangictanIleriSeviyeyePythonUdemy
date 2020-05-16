"""
Author : Arda
Date : 5/8/2020
"""

import mysql.connector as mysql

db = mysql.connect(user='arda',passwd='12345678',host='localhost')

cursor = db.cursor()


def databaseOlustur(cursor , databaseIsmi):
    try:
        cursor.execute(f"CREATE DATABASE {databaseIsmi} DEFAULT CHARACTER SET 'utf8'")
    except Exception as e:
        raise e

def tabloOlustur(cursor):

    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler (isim VARCHAR(20),soyisim VARCHAR(20), cinsiyet VARCHAR(1),yas INT(200), departman VARCHAR(40) )")

    except Exception as e:
        raise e

# tabloOlustur(cursor)

tabloBilgileri = cursor.fetchall()

print(tabloBilgileri)