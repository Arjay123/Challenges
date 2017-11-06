# https://www.hackerrank.com/challenges/equal-stacks/problem
import sys


n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))

def getMaxHeights(*args):
    heights = [sum(h) for h in args]
    hs = [h for h in args]

    while min(heights):
        if heights[1:] == heights[:-1]:
            return heights[0]
        i = heights.index(max(heights))
        heights[i] -= hs[i].pop(0)
    return 0

print getMaxHeights(h1, h2, h3)