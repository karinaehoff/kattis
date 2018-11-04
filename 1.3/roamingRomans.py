'''
Author: Kari Hoff
Filename: roamingRomans.py
Purpose: Roaming Romans on Kattis.com
Date: 3 Nov 2018
'''
import sys
import math

def converter(modernMiles):
    paces = (float(modernMiles))*float(1000*(5280/4854))
    if (paces - int(paces)) >= .5:
        return str(int(paces)+1)
    return str(int(paces))

def main(data):
    task = data.readline().strip()
    sys.stdout.write(converter(task))
    
if __name__ == "__main__":
    main(sys.stdin)