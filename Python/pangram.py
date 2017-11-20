# https://www.hackerrank.com/challenges/pangrams/problem

from string import lowercase as LOWERCASE

s = raw_input()
print "pangram" if len(set(s.replace(' ', '').lower())) == len(LOWERCASE) else "not pangram"