#!/bin/python3

import sys

def primes(limit):
    limitn = limit + 1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i] == True]

m = 1000000
primes_list = primes(m)

def find_sum():
    sum_list = []
    sum = 0
    for i in range(len(primes_list)):
        sum = sum + primes_list[i]
        sum_list.append(sum)

    return sum_list


total_list = find_sum()
array_length = len(primes_list)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
  
    index = 0
    step = 0

    while primes_list[index] <= n:
        step = step + 50
        index = index + step
        if index > array_length:
            break
        
    index = index - step

    while primes_list[index] <= n:
        index = index + 1

    print(total_list[index-1])
