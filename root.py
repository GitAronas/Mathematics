# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:12:54 2023

@author: Amar Doshi
"""

from fractions import Fraction


upperBound: int = None
lowerBound: int = None

_number: int = None
_exp: int = None
_p: Fraction = None

_root:Fraction = None


def bounds(number: int, invExp: int = 2) -> tuple[int, int]:
    """
    Finds the bounds of the nth root of arbitrarily large integers.

    All inputs must be integers > 0

    Note: For performance reasons, input values are not validated.
    """

    if number < 0: return None, None
    if 0 <= number <= 1: return number, number

    l = 0
    h = number

    while l <= h:
        m = (l + h) // 2
        p = m ** invExp

        if p > number:
            h = m - 1
        elif p < number:
            l = m + 1
        elif p == number:
            l = m
            h = m
            break

    global lowerBound, upperBound

    lowerBound = h
    upperBound = l

    return h, l


def root(number: int, invExp: int = 2, iterations: int = 2) -> Fraction:
    """
    Finds the nth root of arbitrarily large integers.

    All inputs must be integers > 0

    Note: For performance reasons, input values are not validated.
    """

    global _number, _exp, _p
    global _root

    _number = number
    _exp = invExp

    l, h = bounds(number, invExp)

    if l == h:
        _root = Fraction(l, 1)
        _p = l ** invExp
    else:
        for _ in range(iterations):
            m = Fraction(l + h, 2)
            p = m ** invExp

            if p > number:
                h = m
            elif p == number:
                break
            elif p < number:
                l = m

        _p = p
        _root = m

    return _root


def mixedFraction() -> tuple[int, Fraction]:
    """
    Returns the root as a mixed fraction.
    """

    d, r = divmod(_root.numerator, _root.denominator)

    return d, Fraction(r, _root.denominator)


def error() -> Fraction:
    """
    Returns (root ** exponent) - number
    """

    return _p - _number


# if __name__ == '__main__':

#     print()

#     n = 27
#     x = 2
#     i = 2

#     r = root(n, x, i)
#     mf = mixedFraction()

#     print(lowerBound, upperBound)
#     print(n ** (1/x))
#     print(r)
#     print(f'{mf[0]}+{mf[1]}')
#     print(error())
