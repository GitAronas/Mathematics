# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:48:29 2023

@author: Amar Doshi
"""

def fibonacci(n: int) -> list:
    '''
    Gives the first n terms of the Fibonacci sequence
    '''
    f = []

    p1 = 0
    p2 = 1

    for _ in range(n):
        p1, p2 = p2, p1 + p2

        f.append(p1)

    return f


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
