#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    maxFec = 0

    while n % 2 == 0:
        maxFec = 2
        n >>= 1

    for i in range(3, int(math.sqrt(n))+1,2):
        while n % i == 0:
            maxFec = i
            n = n/i

    if n > 2:
        maxFec = n

    print(int(maxFec))
