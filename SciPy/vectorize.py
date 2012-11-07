import os
import math
import numpy as np

x = np.linspace(-5.0, 5.0, 10000000)

t0 = os.times()[0]
f = np.vectorize(lambda x: math.exp(-x**2))
fx = f(x)
print "t(vec):", os.times()[0] - t0

t0 = os.times()[0]
fx = [ math.exp(-z**2) for z in x ]
print "t(list):", os.times()[0] - t0

