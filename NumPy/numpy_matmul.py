import os
import numpy as np

A = np.random.rand(500,500)
B = np.random.rand(500,500)

t0 = os.times()[0]
C = np.dot(A,B)
print "t(dot):", os.times()[0] - t0
