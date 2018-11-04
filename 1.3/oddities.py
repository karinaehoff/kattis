'''
Author: Kari Hoff
Filename: oddities.py
Purpose: Oddities on Kattis.com
Date: 27 October 2018
'''
n = int(input())
output = ''
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        output += '{} is even\n'.format(x)
    else:
        output += '{} is odd\n'.format(x)
print(output)