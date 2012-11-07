import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

f = lambda x: np.exp(-x**2)

x = np.linspace(-5.0, 5.0, 200)
xd = np.linspace(-5.0, 5.0, 20)

f1 = interp1d(xd, f(xd))
f2 = interp1d(xd, f(xd), kind='cubic')

plt.plot(x, f(x), 'r', x, f1(x), x, f2(x), xd, f(xd), 'ro')
plt.show()
