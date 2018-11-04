'''
Author: Kari Hoff
Filename: sibice.py
Purpose: Sibice on Kattis.com
Date: 16 October 2018
'''
import math

n, w, h = input().split()
# Number of matches on the floor
n = int(n)
# Dimension 1 of the box
w = int(w)
# Dimension 2 of the box
h = int(h)

hypotenuse = math.sqrt(w**2+h**2)

output = ''
for i in range(n):
    matchLen = int(input())
    if matchLen > hypotenuse:
        output += 'NE\n'
    else:
        output += 'DA\n'
print(output)