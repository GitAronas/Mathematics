# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:05:03 2023

@author: Amar Doshi
"""

from math import sqrt


class Quaternion:

    __slots__ = ('r', 'i', 'j', 'k')

    @staticmethod
    def unit():
        return Quaternion(r=0.5, i=0.5, j=0.5, k=0.5)

    def __init__(self, r=0, i=0, j=0, k=0):
        self.r = r
        self.i = i
        self.j = j
        self.k = k

    def __eq__(self, o):
        return (self.r == o.r
                and self.i == o.i
                and self.j == o.j
                and self.k == o.k)

    def __ne__(self, o):
        return (self.r != o.r
                or self.i != o.i
                or self.j != o.j
                or self.k != o.k)

    def __bool__(self):
        return any((self.r, self.i, self.j, self.k))

    def __neg__(self):
        return Quaternion(-self.r, -self.i, -self.j, -self.k)

    def __add__(self, o):
        return Quaternion(self.r + o.r,
                          self.i + o.i,
                          self.j + o.j,
                          self.k + o.k)

    def __iadd__(self, o):
        self.r += o.r
        self.i += o.i
        self.j += o.j
        self.k += o.k

        return self

    def __sub__(self, o):
        return Quaternion(self.r - o.r,
                          self.i - o.i,
                          self.j - o.j,
                          self.k - o.k)

    def __isub__(self, o):
        self.r -= o.r
        self.i -= o.i
        self.j -= o.j
        self.k -= o.k

        return self

    def __mul__(self, o):
        '''Scalar Multiplication'''
        return Quaternion(o * self.r,
                          o * self.i,
                          o * self.j,
                          o * self.k)

    def __rmul__(self, o):
        '''Scalar Multiplication'''
        return Quaternion(o * self.r,
                          o * self.i,
                          o * self.j,
                          o * self.k)

    '''
    z1 * z2 =
         a*e - b*f - c*g - d*h
    + i (a*f + b*e + c*h - d*g)
    + j (a*g - b*h + c*e + d*f)
    + k (a*h + b*g - c*f + d*e)
    '''

    def __matmul__(self, o):
        '''Quarternion Multiplication'''
        return Quaternion(self.r * o.r - self.i * o.i - self.j * o.j - self.k * o.k,
                          self.r * o.i + self.i * o.r + self.j * o.k - self.k * o.j,
                          self.r * o.j - self.i * o.k + self.j * o.r + self.k * o.i,
                          self.r * o.k + self.i * o.j - self.j * o.i + self.k * o.r)


    def __imatmul__(self, o):
        '''Quarternion Multiplication'''
        r = self.r * o.r - self.i * o.i - self.j * o.j - self.k * o.k
        i = self.r * o.i + self.i * o.r + self.j * o.k - self.k * o.j
        j = self.r * o.j - self.i * o.k + self.j * o.r + self.k * o.i
        k = self.r * o.k + self.i * o.j - self.j * o.i + self.k * o.r

        self.r, self.i, self.j, self.k = r, i, j, k

        return self


    def __truediv__(self, o):
        if isinstance(o, Quaternion):
            raise NotImplementedError()
        else:
            return Quaternion(self.r / o,
                              self.i / o,
                              self.j / o,
                              self.k / o)

    def __itruediv__(self, o):
        if isinstance(o, Quaternion):
            raise NotImplementedError()
        else:
            self.r /= o
            self.i /= o
            self.j /= o
            self.k /= o

        return self

    #TODO Quaternion angle

    def conjugate(self):
        return Quaternion(self.r, -self.i, -self.j, -self.k)

    def norm(self):
        return sqrt(self.r ** 2 + self.i ** 2 + self.j ** 2 + self.k ** 2)

    def normalise(self):
        return self / self.norm()

    def __repr__(self):
        return f'Quarternion({self.r}, {self.i}, {self.j}, {self.k})'

    def __str__(self):
        return f'({self.r}{self.i:+}i{self.j:+}j{self.k:+}k)'



if __name__ == '__main__':

    print()
