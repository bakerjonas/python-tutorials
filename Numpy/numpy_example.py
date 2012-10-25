import numpy as np

a = np.arange(9).reshape(3,3)
b = a**2
c = a + b - 0.5 * a.transpose()
d = b * c  #  element wise
e = np.dot(c, d)  #  matrix multiplication
f = np.sin(e)
g = b < c

print a.sum()
print a.max()

a = np.cos(np.arange(9).reshape(3,3))
print np.linalg.det(a)
print np.linalg.inv(a)
print np.linalg.eig(a)
print np.linalg.norm(a)
print np.linalg.svd(a)
print np.linalg.cholesky(a)
