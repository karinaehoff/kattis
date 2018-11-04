'''
Author: Kari Hoff
Filename: faktor.py
Purpose: Faktor on Kattis.com
Date: 15 October 2018
'''
a, i = input().split()
# Number of Articles
a = int(a)
# Impact Factor
i = int(i)

x = a*i-(a-1)
print(x)

