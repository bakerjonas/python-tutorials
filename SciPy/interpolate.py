import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

f = lambda x: math.exp(-x**2)
x = np.linspace(-5.0, 5.0, 20)
y = np.exp(-x**2)

f1 = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')
fv = np.vectorize(f)
xnew = np.linspace(-5.0, 5.0, 100)

plt.plot(xnew, f1(xnew), xnew, f2(xnew), x, fv(x), 'ro')
plt.show()
