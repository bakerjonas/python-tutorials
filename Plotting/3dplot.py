import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
import numpy as np

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.exp(-1.0*(X**2 + Y**2))

ax = plt.subplot(1, 2, 1, projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim3d(-0.05, 1.01)
plt.colorbar(surf, shrink=0.5, aspect=10)

ax = plt.subplot(1, 2, 2, projection='3d')
ax.set_zlim3d(-0.05, 1.01)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()

