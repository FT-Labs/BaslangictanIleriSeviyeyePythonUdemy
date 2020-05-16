"""
Author : Arda
Date : 4/24/2020
"""

def ikiyeKatla(x , *args):
    ikiyeKatlananListe =    []

    ikiyeKatlananListe.append(x*3)

    for sayi in args:
        ikiyeKatlananListe.append(2*sayi)

    return ikiyeKatlananListe


# sayiListesi = ikiyeKatla(2,1,4,5,10,24,25,28)
stringListesi = ikiyeKatla(3,"b","c","d",2,3,4)

print(stringListesi)


