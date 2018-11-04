'''
Author: Kari Hoff
Filename: quadrantSelection.py
Purpose: ICPC Prep #2 Problem A
Date: 1 October 2018
'''

x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)