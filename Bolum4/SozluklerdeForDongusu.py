"""
Author : Arda
Date : 4/15/2020
"""


meyveAdedi = {"Elma" : 5,
              "Armut" : 7,
              "Portakal" : 11,
              "Çilek" : 57}

# // Hem anahtar hem değerler için (sözlüklerde) for döngüsü çevirmek istiyorsanız .items() fonksiyonunu kullanın.

# for anahtar,deger in meyveAdedi.items():
#     print(anahtar , deger)


#.values() fonksiyonu sözlüklerdeki değerleri çağırır.
# for anahtar in meyveAdedi.values():
#     print(anahtar)

kareler = dict()

for sayi in range(10):
    kareler[sayi] = sayi**2

print(kareler)