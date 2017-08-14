#!/bin/python3

import sys


def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    alice = 0
    bob = 0
    a = [a0, a1, a2]
    b = [b0, b1, b2]

    for i in range(0, 3):
        if (a[i] > b[i]):
            alice += 1
        if (b[i] > a[i]):
            bob += 1
    return (alice, bob)


a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


