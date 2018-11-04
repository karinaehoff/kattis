'''
Author: Kari Hoff
Filename: tarifa.py
Purpose: ICPC Practice Problem A
Date: 14 September 2018
'''

def main():
    X = int(input()) #MG per month
    N = int(input()) #number of months
    mgLeft = 0 #MG left from last month
    for i in range(0, N, 1):
        mgSpent = int(input())
        mgLeft += X - mgSpent
    print(mgLeft + X)
    
if __name__ == "__main__":
    main()