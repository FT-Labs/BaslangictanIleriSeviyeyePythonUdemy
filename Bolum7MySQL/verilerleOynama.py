"""
Author : Arda
Date : 5/8/2020
"""

import mysql.connector as mysql

db = mysql.connect(user = 'arda' , passwd = '12345678' , host = 'localhost' , database = 'calisanlar')

cursor = db.cursor()

# cursor.execute("UPDATE bilgiler SET departman='Yazılım Geliştirme' WHERE isim='Merve'")
# db.commit()
# cursor.execute("UPDATE bilgiler SET yas='31' WHERE isim='Arda'")
# db.commit()

# cursor.execute("ALTER TABLE bilgiler ADD COLUMN calismayili INT(40) AFTER departman")



# calismaYili = 2
# for calisan in calisanlar:
#     query = "UPDATE bilgiler SET calismayili='{}' WHERE isim='{}'".format(calismaYili,calisan[0])
#     cursor.execute(query)
#     calismaYili += 1
#     db.commit()

# cursor.execute("ALTER TABLE bilgiler ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST ")

cursor.execute("SELECT * FROM bilgiler")
print(cursor.fetchall())


cursor.execute("SELECT * INTO OUTFILE 'calisanlar.csv' CHARACTER SET utf8 FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '\' LINES TERMINATED BY '\n' FROM bilgiler")

