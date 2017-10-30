# https://www.hackerrank.com/challenges/dynamic-array/problem

N, Q = map(int, raw_input().split())
seqList = [[] for _ in range(N)]
lastAnswer = 0

for _ in range(Q):
    qType, x, y = map(int, raw_input().split())
    seq = seqList[(x ^ lastAnswer) % N]
    if qType == 1:
        seq.append(y)
    else:
        lastAnswer = seq[y % len(seq)]
        print lastAnswer