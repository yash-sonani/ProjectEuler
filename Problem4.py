#!/bin/python3

import sys


def check_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    r = 0
    for p in range(999, 100, -1):
        for q in range(999, 100, -1):
            t = p * q
            if t < n:
                if r < t and check_palindrome(str(t)):
                    r = t
                    break
                elif t < r:
                    break

    print(r)
