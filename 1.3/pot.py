'''
Author: Kari Hoff
Filename: pot.py
Purpose: Pot on Kattis.com
Date: 16 October 2018
'''
numbers = []
n = int(input())
for i in range(n):
    addends = input()
    numbers.append(int(addends[0:-1])**int(addends[-1]))
summation = 0
for number in numbers:
    summation += number
    
print(summation)