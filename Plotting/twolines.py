import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)
line1, = plt.plot(x, np.sin(x), '--', linewidth=2)
line2, = plt.plot(x, np.cos(x), '-o', linewidth=2)

dashes = [10, 5, 50, 5] # 10 points on, 5 off, 50 on, 5 off
line1.set_dashes(dashes)
plt.title("sin(x) w/ custom dashes")

plt.show()
#plt.savefig('lines.pdf')
