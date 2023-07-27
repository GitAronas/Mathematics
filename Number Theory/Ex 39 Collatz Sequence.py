# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:48:29 2023

@author: Amar Doshi
"""

def collatz(startingNumber):
    if startingNumber < 1: return []

    s = [startingNumber]

    while  startingNumber > 1:
        if startingNumber % 2 == 0:
            startingNumber //= 2
            s.append(startingNumber)
        else:
            startingNumber = 3 * startingNumber + 1
            s.append(startingNumber)

    return s


assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123

import random
random.seed(42)

for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)

assert seq[0] == startingNum # Make sure it includes the starting number.
assert seq[-1] == 1 # Make sure the last integer is 1.
