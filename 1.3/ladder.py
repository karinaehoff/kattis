'''
Author: Kari Hoff
Filename: ladder.py
Purpose: Ladder on Kattis.com
Date: 4 November 2018
'''

import sys
import math

def main(data):
    
    h, v = data.readline().strip().split()
    h = int(h)
    v = int(v)
    # angle is the ratio of opposite side to the hypotenuse
    #sin(a) = opposite/hypotenuse
    
    ans = math.ceil((h/math.sin(math.radians(v)))*math.sin(math.radians(90)))
            
    sys.stdout.write('{}\n'.format(ans))

if __name__ == "__main__":
    main(sys.stdin)