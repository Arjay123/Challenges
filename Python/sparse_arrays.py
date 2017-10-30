# https://www.hackerrank.com/challenges/sparse-arrays/problem

N = int(raw_input())
strs = {}

for _ in range(N):
    s = raw_input()
    strs[s] = strs.get(s, 0) + 1

Q = int(raw_input())

for _ in range(Q):
    print strs.get(raw_input(), 0)