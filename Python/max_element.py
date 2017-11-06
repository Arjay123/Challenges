# https://www.hackerrank.com/challenges/maximum-element/problem

s = []
max_s = []

N = int(raw_input())

for _ in range(N):
    query = map(int, raw_input().split(' '))
    if query[0] == 1:
        s.append(query[1])
        if not len(max_s) or query[1] > max_s[-1]:
            max_s.append(query[1])
        else:
            max_s.append(max_s[-1])
    elif query[0] == 2:
        s.pop()
        max_s.pop()
    elif query[0] == 3:
        print max_s[-1]