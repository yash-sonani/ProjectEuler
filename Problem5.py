#!/bin/python3

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    ans = 1
    for i in range(1, n + 1, 1):
        ans = (ans * i)/math.gcd(int(ans), i)

    print(int(ans))
