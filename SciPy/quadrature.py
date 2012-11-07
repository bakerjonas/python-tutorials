import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

f = lambda x: np.exp(-x**2)
I = quad(f, -10.0, 10.0)
print "Quadrature:", I
print "Exact:", math.sqrt(math.pi)

x = np.linspace(-5.0, 5.0, 100)
xd =  np.linspace(-5.0, 5.0, 31)
fd = np.vectorize(lambda x: math.exp(-x**2))
plt.plot(x, f(x), xd, fd(xd), 'ro')
plt.show()
