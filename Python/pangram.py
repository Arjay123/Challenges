# https://www.hackerrank.com/challenges/pangrams/problem

"""
Because the characters of the string s are constrained to spaces or alphabetic
letters, we can simply create a set from a lowercase version of the string s.

Because of the properties of a set, we can check if the length of the set
equals the length of a string containing all the letters of the alphabet (26).
"""
from string import lowercase as LOWERCASE

s = raw_input()
print "pangram" if len(set(s.replace(' ', '').lower())) == len(LOWERCASE) else "not pangram"