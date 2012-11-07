#!/usr/bin/env python
import pp
import math
from scipy.integrate import quad
import scipy.integrate 

n = 4
ival = (-20.0, 20.0)
step = sum(map(abs, ival))/n

server = pp.Server(n)

def f(x): 
    return math.exp(-0.1*x**2)

def integrate(f, a, b): 
    '''Wrapper for quad so name resolution works'''
    return scipy.integrate.quad(f, a, b)

foo = lambda i: (ival[0] + i * step, ival[0] + (i + 1) * step)
view = [ foo(i) for i in range(n)]

p = []
for i in range(n):
    a, b = view[i]
    p.append(server.submit(integrate, (f, a, b), (f,), ('math',
        'scipy.integrate')))

I = 0.0
for i in range(n):
    r = p[i]()
    I += r[0]

a, b = ival
print I, quad(f, a, b)[0]
print server.print_stats()
