#!/bin/python3

import sys


def find_num_list(num, n, k):
    num_list = []

    for i in range(n - k + 1):
        num_list.append(int(num[i:i + k]))

    return num_list


def find_max_prod(num_list):

    max_product = 0

    for i in num_list:
        if "0" not in str(i):

            prod = 1
            while (i > 0):
                rem = i % 10
                prod = prod * rem
                i = i // 10

            if prod > max_product:
                max_product = prod

    return max_product

t = int(input().strip())

for a0 in range(t):
    n, k = input().strip().split(' ')
    num = input().strip()
    n, k = [int(n), int(k)]

    # Find all substring
    number_list = find_num_list(str(num), n, k)

    # Find Maximum Product
    maximum_product = find_max_prod(number_list)
    print(maximum_product)
