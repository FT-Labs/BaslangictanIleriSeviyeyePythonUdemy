"""
Author : Arda
Date : 4/11/2020
"""

list2 = ["portakal" , "çilek" , "muz" , "mango" , "ananas"]


# for i in range(len(list2)):               Farklı yazım tipi
#     print(f"{i} = {list2[i]}")

# list1.append(9)       append() komutu ile listeye yeni elemanlar eklenebilir.

# print(sorted(list1))      sorted() fonksiyonu ile elemanlar küçükten büyüğe sıralanabilir. (1 sefere mahsus)

# list1.remove(8)       [].remove(eleman)       Belirtilen elamanı listeden çıkartırç
# list1.pop()         [].pop()      Son elemanı listeden çıkartır, içine index girilirse belirlenen elemanı çıkartır.

# list1.insert(1 , 7)       .insert() komutu belirlenen indexe yeni bir eleman ekler.

# list2.reverse()       .reverse() komutu listenin sıralamasını ters çevirir.

# for i in reversed(range(10)):         reversed() komutu sıralamayı tersine çevirir.
#     print(i)

# list2 = list1.copy()          copy() komutu listeyi kopyalar.

list1 = [5 , 11 , 3 , 4 , 8]

# print(sorted(list1 , reverse= True))  Listeyi 1 sefere mahsus büyükten küçüğe doğru sıralar.

list1.sort()
list1.reverse()
print(list1)
