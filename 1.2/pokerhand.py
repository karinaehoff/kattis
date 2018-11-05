'''
Author: Kari Hoff
Filename: pokerHand.py
Purpose: Poker Hand on Kattis.com
Date: 4 November 2018
'''

import sys

def main(data):
    k_dict = {}
    for _ in 'A23456789TJQK':
        k_dict[_] = 0
    hand = data.readline().strip().split()
    for card in hand:
        rank = card[0]
        k_dict[rank] += 1

    ans = 0
    for _ in k_dict:
        if k_dict[_] > ans:
            ans = k_dict[_]
            
    sys.stdout.write('{}\n'.format(ans))

if __name__ == "__main__":
    main(sys.stdin)