#!/bin/python3

import sys

t = int(input().strip())


def primes_sieve1(limit):
    limitn = limit + 1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i] == True]


result = primes_sieve1(104800)

for a0 in range(t):
    n = int(input().strip())
    print(result[n - 1])
