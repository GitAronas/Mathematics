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

    '''z1 * z2 =
         a*e - b*f - c*g - d*h
    + i (a*f + b*e + c*h - d*g)
    + j (a*g - b*h + c*e + d*f)
    + k (a*h + b*g - c*f + d*e)'''

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

    #TODO Quaternion division & inverse

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

    # c = 1 + 2j

    # print(c, type(c))

    # print(c.__repr__(), type(c.__repr__()))
    # print(c.__str__(), type(c.__str__()))

    q = Quaternion(1,2,3,4)

    # print(q.r, q.i, q.j, q.k)

    # print(q.__repr__())
    # print()
    # print(q.__str__())
    # print()
    # print(q)

    # q.r = 0
    # print(q)

    # q.z = 5
    # print(q.z)

    # print(q.norm())
    # print()
    # print(q.conjugate(), type(q.conjugate()))

    # if q:
    #     print(True)

    # if Quaternion():
    #     print(True)
    # else:
    #     print(False)

    # t = q
    # print(t)

    # t = Quaternion(4,3,2,1)
    # print(t + q)

    # t = Quaternion(4,3,2,1)
    # print(t - q)

    # t = Quaternion(4,3,2,1)
    # print(q - t)

    # print(Quaternion(1,2,3,4) == Quarternion(1,2,3,4))
    # print()
    # print(Quaternion(1,2,3,4) == Quarternion(0,2,3,4))

    # print(Quaternion(1,2,3,4) != Quarternion(1,2,3,4))
    # print()
    # print(Quaternion(1,2,3,4) != Quarternion(0,2,3,4))

    # print(5 * q)
    # print()
    # print(q * -5)

    # print(q / 2)

    # q += Quaternion(4,3,2,1)
    # print(q)

    # q -= Quaternion(4,3,2,1)
    # print(q)

    # q /= 2
    # print(q)

    # print(-q)

    # print(-Quaternion())
    # print()
    # print(Quaternion().conjugate())

    # print(Quaternion(1,2,3,4) @ Quaternion(4,3,2,1))

    # print(q @ q.conjugate())
    # print(Quaternion() @ Quaternion().conjugate())

    # print(Quaternion().norm())

    # q @= q.conjugate()
    # print(q)

    # t = Quaternion()
    # print(t)
    # print(t.norm())

    # print(Quaternion.unit())
    # print()
    # print(Quaternion())

    print(q.normalise())
