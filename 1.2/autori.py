'''
Author: Kari Hoff
Filename: autori.py
Purpose: Autori on Kattis.com
Date: 15 October 2018
'''
names = input().split('-')
output = ''
for name in names:
    output+=name[0]
print(output)