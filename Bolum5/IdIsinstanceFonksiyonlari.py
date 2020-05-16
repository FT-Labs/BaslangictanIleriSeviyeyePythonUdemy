"""
Author : Arda
Date : 4/24/2020
"""

# == YERİNE SAKIN is KULLANMAYIN.

# a = 3
# b = 3
#
# c = "a"
# d = "a"
#
# print(id(c))
# print(id(d))
#
# # if a is b:
# #     print("Koşul doğru")
#
# print(id(a))
# print(id(b))

# liste1 = (1,2)
# liste2 = liste1
#
# print(id(liste1))
# print(id(liste2))


class Insan:
    def __init__(self , isim):
        self.isim = isim


zeynep = Insan("Zeynep")

if isinstance(zeynep , Insan):
    print("Kosul dogru.")


a = [1,2]
b = a


