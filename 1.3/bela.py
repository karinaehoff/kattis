'''
Author: Kari Hoff
Filename: bela.py
Purpose: Bela on Kattis.com
Date: 4 November 2018
'''

import sys

def main(data):
    
    N, B = data.readline().strip().split()
    N = int(N)
    non_dom_card_values = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}
    dom_card_values = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}

    ans = 0

    for i in range(4*N):
        card = data.readline().strip()
        value = card[0]
        suit = card[1]
        if suit == B:
            ans += dom_card_values[value]
        else:
            ans += non_dom_card_values[value]

            
    sys.stdout.write('{}\n'.format(ans))

if __name__ == "__main__":
    main(sys.stdin)