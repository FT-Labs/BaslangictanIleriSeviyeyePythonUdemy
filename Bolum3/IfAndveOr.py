"""
Author : Arda
Date : 4/10/2020
"""

# bağlaç 1-> or : İlk durum ya da ikinci durum doğruysa çalıştırılır, iki durumda yanlışsa atlanır
# bağlaç 2-> and : İki durumda doğruysa çalıştırılır, aksi taktirde atlanır


a = 13
b = 25
c = 45
#İf döngüsüyle en yüksek sayıyı bulun
# if a>b and a>c:
#     print("a en büyük sayıdır.")
# elif b>a and b>c:
#     print("b en büyük sayıdır.")
# elif c>a and c>b:
#     print("c en büyük sayıdır.")

d = -10
e = 12

# if d>e or d>0:
#     print("d e'den büyük yada 0'dan büyük olabilir.")

#Short-hand if

f = 150
g = 20

#if f<g: print("f g'den küçüktür.")

print("f g'den küçüktür") if f<g else print("f g'den büyüktür")