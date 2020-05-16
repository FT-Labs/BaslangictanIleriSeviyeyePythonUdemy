"""
Author : Arda
Date : 4/24/2020
"""

def sozlukItemleri(x , **kwargs):
    print(f"Arda {x} sayısını çok seviyor.")

    for anahtar, deger in kwargs.items():
        print(f"{anahtar}'ın değeri : {deger}")


sozlukItemleri(20 , isim = "arda" , yas = 15 , boy = 188 , irk = "Türk")

