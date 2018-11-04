'''
Author: Kari Hoff
Filename: pet.py
Purpose: Pet on Kattis.com
Date: 27 October 2018
'''
scores = {}
winner = 0
for i in range(5):
    grades = input().split()
    score = 0
    for grade in grades:
        grade = int(grade)
        score += grade
    scores[score] = i+1
    winner = max(winner, score)
print(scores[winner], winner)


    