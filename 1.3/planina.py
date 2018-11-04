'''
Author: Kari Hoff
Filename: planina.py
Purpose: Planina on Kattis.com
Date: 16 October 2018
'''

import sys
import math

def num_of_squares(n):
    return 4**n

def main(data):
    iterations = int(data.readline().strip())
    
    squares = num_of_squares(iterations)
    numberOfPoints = int((math.sqrt(squares)+1)**2)
    
    sys.stdout.write(str(numberOfPoints))
    
if __name__ == "__main__":
    main(sys.stdin)