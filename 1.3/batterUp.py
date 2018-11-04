'''
Author: Kari Hoff
Filename: batterUp.py
Purpose: ICPC Practice Problem B
Date: 14 September 2018
'''

def main():
    n = int(input()) #number of at-bats
    N = input().strip().split() #n integers seperated by spaces
    #N.split()
    bases = 0
    hits = 0
    for num in N:
        num = int(num)
        if num!=-1:
            if num!=0:
                bases += num
            hits +=1
    slug = bases/hits
    print(slug)

if __name__ == "__main__":
    main()