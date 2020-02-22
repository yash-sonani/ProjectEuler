#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    ans = math.pow(n * (n + 1) / 2, 2) - (n * (n + 1) * (2*n + 1))/6

    print(int(ans))
