#!/usr/bin/env python

def f(x):
    return x**2-x

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

if __name__ == '__main__':
    I = integrate_f(0.0, 100.0, 10000000)
    print I
