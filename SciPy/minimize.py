import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin

f = lambda x: 0.01*(x-2.0)**4 + x**3 - 4.0*x**2 + x
minx = fmin(f, 4.0)
print "Minimum:", minx, f(minx)

x = np.linspace(0.0, 5.0, 100)
plt.plot(x, f(x), minx, f(minx), 'ro')
plt.show()
