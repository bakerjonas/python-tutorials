import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

def f(x, p = [0.01, 1.0, 3.0]):
    a, b, c = p
    return a*(x-2.0)**4 + b*x**3 - c*x**2 + x

def residual(p, y, x):
    return y - f(x, p)

x = np.arange(0.0, 5.0, 0.1)
measured = f(x) + 2 * np.random.randn(len(x))

fit = leastsq(residual, (1.0, 2.0, 5.0), args=(measured, x))
print "Fit parameters:", fit

plt.plot(x, f(x), 'r', x, measured, 'ob', x, f(x, fit[0]))
plt.show()
