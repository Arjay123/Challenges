# https://www.hackerrank.com/challenges/balanced-brackets/problem

import sys

OPENERS = "{[("
CLOSERS = "}])"

def tagMatchesOpening(open, close):
    return OPENERS[CLOSERS.index(close)] == open

def isBalanced(s):
    stac = []

    for bracket in s:
        if bracket in OPENERS:
            stac.append(bracket)
        else:
            if not len(stac) or not tagMatchesOpening(stac[-1], bracket):
                return "NO"
            stac.pop()
    return "NO" if stac else "YES"

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        s = raw_input().strip()
        result = isBalanced(s)
        print result