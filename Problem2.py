#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    if not n < 2:

        n1=0
        n2=2
        sum = n1 + n2

        while(n2 < n):

            n3 = 4 * n2 + n1

            if n3 > n:
                break

            n1 = n2
            n2 = n3
            sum = sum + n2

        print(sum)
