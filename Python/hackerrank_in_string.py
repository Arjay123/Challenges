# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

#!/bin/python

import sys

"""
Because the substring 'hackerrank' must appear in the string s in order, we can
create a chunk of the string s, where we search for the next character in
'hackerrank'. If at any point, the next character in hackerrank does not exist
in the string s, then we can exit the loop.
"""
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

