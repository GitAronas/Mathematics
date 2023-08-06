# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:48:29 2023

@author: Amar Doshi
"""

def fibonacci(n: int) -> list[int]:
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


def collatz(startingNumber: int) -> list[int]:
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


def triangularNumbers(n: int) -> list[int]:
    m = 0
    t = []
    
    for i in range(1, n + 1):
        m += i
        t.append(m)
        
    return t


'''
Lucky Numbers:
-------------

Begin with a list of integers starting with 1 :
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, . . . .
Now eliminate every second number :
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, ...
The second remaining number is 3, so remove every 3rd number:
1, 3, 7, 9, 13, 15, 19, 21, 25, ...
The next remaining number is 7, so remove every 7th number:
1, 3, 7, 9, 13, 15, 21, 25, ...
Next, remove every 9th number and so on.
Finally, the resulting sequence is the lucky numbers.

https://www.w3resource.com/python-exercises/math/
'''

def luckyNumbers(n: int) -> list[int]:
    l = [0] + list(range(1, n + 1, 2))

    ln = len(l)

    p1 = 2

    while (p2 := l[p1]) < ln:
        n = p2 - 1

        print(p1, p2, ln)

        while p2 < ln:
            l.pop(p2)
            ln -= 1
            p2 += n

        p1 += 1

    return l[1:]
