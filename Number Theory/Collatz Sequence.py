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
