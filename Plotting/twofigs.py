import numpy as np
import matplotlib.pyplot as plt

plt.figure(0)
x = np.linspace(0, 10)
line1, = plt.plot(x, np.sin(x), '--', linewidth=2)

plt.figure("Hi!")
line2, = plt.plot(x, np.cos(x), '-o', linewidth=2)
plt.title("cos(x)")

plt.figure(0)
plt.title("sin(x)")

plt.savefig('lines.png')
plt.show()
