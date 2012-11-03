# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>
# <codecell>

x=1
if x is None:
    x=0
    print('Undefined, set to zero')
elif x == 0:
    print('Zero')
elif x < 0:
    print('Negtive')
else:
    print('Positive')

# <codecell>

n=0
while n < 100:
    print('All work and no play')
    if n == 10:
        n += 10
        continue
    elif n == 25:
        break
    n += 1

# <codecell>

foo = [1, 2, 75, 6, 7, 'tjohej!']
for i in foo:
    print(i)
for i in range(100):
    if i % 10 == 0:
        print(i)
else:
    pass
print(range(1,10, 2))


# <codecell>

def foobar(x, y):
    a=x+y
    return a, a**2
i, j = foobar(2,3)

# Dynamic nature of Python:

def raboof(x, y=5):
    return x**y * raboof.foo
raboof.foo = 0.1

print(raboof(2))

# <codecell>

f = open('foo.txt', 'w')
for i in range(5):
    print >> f, ("   Line number %d  " % i)

# <codecell>

f = open('foo.txt', 'r')
print(f.readlines())

g = open('bar.txt', 'w')

f.seek(0) # Rewind the file
for i in f:
    l = i.strip().split()
    if len(l) > 0:
        print >> g, (l[2]) 
f.close()
g.close()


# <codecell>

import sys
from os import environ
import numpy as np

print(sys.path, environ['PATH'])
a = np.array([1, 2, 3])
dir(sys)
dir(a)
dir(1)

 

# <codecell>

class Foobar:
    bar = True
    
    def __init__(self, x):
        self.foo = x

    def __str__(self):
        return 'Foobar is %d %r.' % (self.foo, self.bar)

    def double(self):
        self.foo *= 2
        return self.foo


# <codecell>

a = Foobar(1)
b = Foobar(42)
print(a, b )# invokes __str__()
print(b.double())
Foobar.bar = False # set global class variable
print(a, b)


# <codecell>

import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
c = np.zeros((5, 5))
d = np.arange(0,4).reshape(2,2)
e = np.ndarray((10, 10, 100), dtype='float')
f = np.array(e)
g = np.ones_like(d)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


# <codecell>

a = np.random.rand(5,5)
print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype.name)
print(a)


# <codecell>

a = np.arange(9).reshape(3,3)
b = a**2
c = a + b - 0.5 * a.transpose()
d = b * c # element wise
e = np.dot(c, d) # matrix multiplication
f = np.sin(e)
g=b<c
a.sum()
a.min()
a.max()


# <codecell>

from numpy import linalg
a = np.cos(np.arange(9).reshape(3,3))
linalg.det(a)
linalg.inv(a)
linalg.eig(a)
linalg.norm(a)
linalg.svd(a)

i = np.arange(3)
a[i,i] += 2
linalg.cholesky(a)


# <codecell>

a = np.random.rand(10,10)
print(a[3, 4])
print(a[1, :])
print(a[0:4, 6:9])
for row in a:
    print(row)

for i in np.nditer(a):
    print(i)

# <codecell>


