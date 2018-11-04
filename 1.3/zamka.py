'''
Author: Kari Hoff
Filename: zamka.py
Purpose: Zamka on Kattis.com
Date: 15 October 2018
'''

# Lower bound
l = int(input())
# upper bound
d = int(input())
# sum
x = int(input())

def check_sum_of_digits(num):
    total = 0
    num_str = str(num)
    for ch in num_str:
        total+=int(ch)
    return total

# Minimum Integer
n = l
while check_sum_of_digits(n) != x:
    n+=1  
print(n)

# Maximum Integer
m = d
while check_sum_of_digits(m) != x:
    m-=1  
print(m)