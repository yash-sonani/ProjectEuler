#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    product = -1;
    a = 1
    while a <= n / 3:

        b = int((n * n - 2 * n * a) / (2 * n - 2 * a))

        c = n - a - b

        if c * c == (a * a + b * b):
            temp = a * b * c

            if temp > product:
                product = temp
        a = a + 1
    print(product)
