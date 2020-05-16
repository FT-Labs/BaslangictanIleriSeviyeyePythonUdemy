"""
Author : Arda
Date : 5/1/2020
"""

import os

# print(os.environ)

# print(os.getcwd())       Programınızın şuanki çalışma konumunu döner

# os.chdir("C:/Users/PhysTech/Desktop/Udemy/")  Programınızın çalışma konumunu değiştirir

# os.mkdir("Python")  Klasör üretmeye yarar

# os.makedirs("Python/Python1/python3")  Birden fazla içiçe klasör oluşturmaya yarar

# os.rmdir("Python/Python1/python3")    Bir klasörü boş ise siler

# os.removedirs("Python/Python1")       Birden fazla klasörü silmeye yarar

#os.walk() dosyalar üzerinde gezinmeye yarar

# for kok , klasorler , dosyalar in os.walk("C:/Users/PhysTech/Desktop/Udemy/PythonVideos"):
#     print(kok)
#     print(klasorler)
#     print(dosyalar)

# os.startfile("MailEki.txt")   Bilgisayardaki bir dosyayı açmaya yarar

# os.remove("bos.py")    Bilgisayarınızdaki dosyayı silmeye yarar

os.chdir("C:/Users/PhysTech/Desktop/Udemy/PythonVideos")


# for klasor in os.listdir():           os.listdir() dizin içindeki dosyaları yazdırır
#     print(klasor)
#
#     for dosya in os.listdir(klasor):
#         print(dosya)







