# https://www.hackerrank.com/challenges/arrays-ds

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

print ' '.join([str(x) for x in arr[::-1]])
