from numpy import linspace, sin
x = linspace(0, 10, 100) # create 100 numbers between 0 and 10

import matplotlib.pyplot as plt
plt.plot(x, sin(x))
# Show GUI with plot. Not necessary if run interactively from pylab
plt.show() # blocking