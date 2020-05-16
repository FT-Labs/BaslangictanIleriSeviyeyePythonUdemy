"""
Author : Arda
Date : 4/15/2020
"""

# a = [x%2 for x in range(10)]
# a = [x**2 for x in range(10)]
# a = [x for x in range(100)]

# a = [x%3 == 0 for x in range(30)]

a = [x**2 for x in range(20) if x%2==0]

print(a)