#!/usr/bin/env python

import os
import cyquad

def f(x):
    return x**2-x

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

if __name__ == '__main__':
    t0 = os.times()[0]
    I = integrate_f(0.0, 100.0, 10000000)
    print "I = {}\n  t(I) = {}".format(I, os.times()[0] - t0)

    t0 = os.times()[0]
    I = cyquad.integrate_f(0.0, 100.0, 10000000)
    print "I = {}\n  t(I) = {}".format(I, os.times()[0] - t0)

