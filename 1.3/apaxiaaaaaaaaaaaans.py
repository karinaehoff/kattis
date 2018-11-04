'''
Author: Kari Hoff
Filename: apaxiaaaaaaaaaaaans.py
Purpose: Apaxiaaaaaaaaaaaans on Kattis.com
Date: 15 October 2018
'''
name = input()
output = ''
previousLetter = name[0]
for ch in name[1:]:
    if ch != previousLetter:
        output+=previousLetter
        previousLetter = ch
output+=previousLetter
print(output)