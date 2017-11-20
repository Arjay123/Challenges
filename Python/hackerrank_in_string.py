# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

#!/bin/python

import sys


q = int(raw_input().strip())

for a0 in xrange(q):
    s = raw_input().strip()
    check = "hackerrank"
    check_s = 0

    while check and check_s < len(s):
        res = s[check_s:].find(check[0])
        if res == -1:
            break
        check = check[1:]
        check_s += res+1

    if check:
        print "NO"
    else:
        print "YES"

