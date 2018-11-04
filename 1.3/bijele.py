'''
Author: Kari Hoff
Filename: bijele.py
Purpose: Bijele on Kattis.com
Date: 15 October 2018
'''
currentSet = input().split()
for i in range(6):
    currentSet[i] = int(currentSet[i])
correctSet = [1,1,2,2,2,8]
output = []
for i in range(6):
    output.append(str(correctSet[i]-currentSet[i]))
output = ' '.join(output)
print(output)
