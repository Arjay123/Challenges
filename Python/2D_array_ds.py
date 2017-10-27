#https://www.hackerrank.com/challenges/2d-array/problem

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

max_sum = None

for x in range(0, len(arr)-2):
    for i in range(0, len(arr)-2):
        sum = arr[x][i] + arr[x][i+1] + arr[x][i+2] + arr[x+1][i+1] + arr[x+2][i] + arr[x+2][i+1] + arr[x+2][i+2]
        if max_sum is None or sum > max_sum:
            max_sum = sum

print max_sum