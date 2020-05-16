"""
Author : Arda
Date : 4/24/2020
"""

import time


# print("Programı 2 saniye durduruyorum.")
# time.sleep(5)
# print("Zaman durdumu?")           #time.sleep() programı verilen saniye cinsinden durdurur.

# suankiZaman = time.ctime()    ctime() şuanki tarihi ve zamanı döner.
# print(suankiZaman)

# baslangicZamani = time.time()
# print(baslangicZamani)
# for sayi in range(100000000):
#     pass
# bitisZamani = time.time()
# print(bitisZamani - baslangicZamani)


lokalZaman = time.localtime()
okunabilirZaman = time.strftime("%d.%m.%Y ; %H:%M:%S", lokalZaman)
print(okunabilirZaman)
