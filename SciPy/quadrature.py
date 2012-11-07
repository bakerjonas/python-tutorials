import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import quad

f = lambda x: math.exp(-x**2)

I = quad(f, -10.0, 10.0)
print "Quadrature:", I
print "Exact:", math.sqrt(math.pi)

vec_f = np.vectorize(f)
x = np.arange(-5.0, 5.0, 0.1)

plt.plot(x, vec_f(x))
plt.show()
