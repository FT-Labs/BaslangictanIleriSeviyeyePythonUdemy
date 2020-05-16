"""
Author : Arda
Date : 4/30/2020
"""


# Fibonacci Serisi : 1 , 1 , 2 , 3 , 5 , 8 ...


def fibonacciBul(sayi):

    a , b = 0 , 1

    for _ in range(sayi):

        a , b = b , a + b
        yield str(a)



girdi = int(input("Fibonacci serisinin bulunmasını istediğiniz eleman sayısını girin.\n"))

fiboList = list(fibonacciBul(girdi))

print(",".join(fiboList))

