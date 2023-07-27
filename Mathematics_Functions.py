# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:31:33 2023

@author: Amar Doshi
"""


def gcd(n1: int, n2: int) -> int:
    while n2 > 0:
        n1, n2 = n2, n1 % n2

    return n1


def lcm(n1: int, n2: int) -> int:
    return (n1 * n2) // gcd(n1, n2)


def fact(start: int, end: int = 2) -> int:
    '''
    Start value > end value

    Both start and end values are inclusive
    '''

    f = 1

    for i in range(end, start + 1):
        f *= i

    return f


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


