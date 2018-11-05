'''
Author: Kari Hoff
Filename: everywhereMan.py
Purpose: I've Been Everywhere, Man on Kattis.com
Date: 4 November 2018
'''

import sys
import math

def main(data):
    
    t = int(data.readline().strip())
    
    ans = ''

    for i in range(t):
        cities = set()
        n = int(data.readline().strip())
        for i in range(n):
            cities.add(data.readline().strip())
        ans += str(len(cities)) + '\n'
            
    sys.stdout.write('{}'.format(ans))

if __name__ == "__main__":
    main(sys.stdin)