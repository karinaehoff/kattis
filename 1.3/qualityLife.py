'''
Author: Kari Hoff
Filename: qualityLife.py
Purpose: Quality-Adjusted Life-Year on Kattis.com
Date: 4 November 2018
'''

import sys

def calcQALY(q, y):
    return q * y

def main(data):
    N = int(data.readline().strip())
    ans = 0
    for i in range(N):
        q, y = data.readline().strip().split()
        q = float(q)
        y = float(y)
        ans += calcQALY(q, y)
    sys.stdout.write('{:.6}\n'.format(ans))

if __name__ == "__main__":
    main(sys.stdin)