"""
Author : Arda
Date : 4/13/2020
"""


def toplam(x , y):
    return x+y
def cikar(x , y):
    return x-y
def bolum(x , y):
    return x/y
def carpim(x , y):
    return x*y

while True:
    try:
        sayi1 = int(input("İlk sayıyı girin."))
        sayi2 = int(input("İkinci sayıyı girin."))

        islem = input("""
Lütfen yapılmasını istediğiniz işlemi girin.
İşlemler : (+ , - , * , /)
Çıkış için 'q' ya basın.
""")

        if islem == 'q':
            break
        elif islem == "+":
            toplam = toplam(sayi1 , sayi2)
            print(f"Sayıların Toplamı : {toplam}")
        elif islem == "-":
            fark = cikar(sayi1 , sayi2)
            print(f"Sayıların Farkı : {fark}")
        elif islem == "*":
            carpim = carpim(sayi1 , sayi2)
            print(f"Sayıların Çarpımı : {carpim}")
        elif islem == "/":
            bolum = bolum(sayi1 , sayi2)
            print(f"Sayıların Bölümü : {bolum}")
        else:
            print("Lütfen geçerli bir işlem girin.")
    except:
        print("Lütfen sayıları doğru girin.")