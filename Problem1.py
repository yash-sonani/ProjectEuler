# Project Euler #1: Multiples of 3 and 5

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    N = n-1
    S1 = (((N // 3)) * (2 * 3 + (N //3 - 1) * 3) //2) 
    S2 = (((N // 5)) * (2 * 5 + (N // 5 - 1) * 5) // 2) 
    S3 = (((N // 15)) *(2 * 15 + (N // 15 - 1) * 15) // 2) 

    print(S1+S2-S3)
