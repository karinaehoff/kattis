'''
Author: Kari Hoff
Filename: awards.py
Purpose: ICPC awards on Kattis.com
Date: 4 November 2018
'''

import sys

def main(data):
    
    N = int(data.readline().strip())

    winningSchools = set()

    ans = []

    for i in range(N):
        university, team = data.readline().strip().split()
        if university not in winningSchools:
            winningSchools.add(university)
            ans.append(university + ' ' + team)

    for i in range(12):
        sys.stdout.write('{}\n'.format(ans[i]))

if __name__ == "__main__":
    main(sys.stdin)