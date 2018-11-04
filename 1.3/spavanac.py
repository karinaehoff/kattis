'''
Author: Kari Hoff
Filename: spavanac.py
Purpose: Spavanac on Kattis.com
Date: 15 October 2018
'''
hour, minute = input().split()
hour = int(hour)
minute = int(minute)
newMinute = minute-45
newHour = hour
if newMinute < 0:
    newHour-=1
    if newHour < 0:
        newHour = 23
    newMinute+=60
    
print(newHour,newMinute)