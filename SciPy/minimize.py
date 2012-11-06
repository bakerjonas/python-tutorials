import numpy as np
from scipy.optimize import fmin
import matplotlib
import matplotlib.pyplot as plt

f  = lambda x: 0.01*(x-2.0)**4 + x**3 - 4.0*x**2 + x

x = np.arange(0.0, 5.0, 0.1)
discrete_f = np.vectorize(f)

mx = fmin(f, 4.0)

plt.plot(x, discrete_f(x), mx, f(mx), 'ro')
plt.show()
