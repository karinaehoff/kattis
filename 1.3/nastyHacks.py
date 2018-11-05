'''
Author: Kari Hoff
Filename: nastyHacks.py
Purpose: nastyHacks on Kattis.com
Date: 4 November 2018
'''

import sys

def main(data):
    
    n = int(data.readline().strip())
    output = ''
    for i in range(n):
        r, e, c = data.readline().strip().split()
        r = int(r)
        e = int(e)
        c = int(c)
        worthIt = e - c
        if worthIt > r:
            output += 'advertise\n'
        elif worthIt < r:
            output += 'do not advertise\n'
        else:
            output += 'does not matter\n'
            
    sys.stdout.write('{}'.format(output))

if __name__ == "__main__":
    main(sys.stdin)