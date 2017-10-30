# https://www.hackerrank.com/challenges/array-left-rotation?h_r=next-challenge&h_v=zen

import sys

def leftRotation(a, d):
    return a[d:] + a[:d]

if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = map(int, raw_input().strip().split(' '))
    result = leftRotation(a, d)
    print " ".join(map(str, result))
