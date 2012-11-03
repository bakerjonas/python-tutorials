a = np.arange(9).reshape(3,3)
b = a**2
c = a + b - 0.5 * a.transpose()
d = b * c # element wise
e = np.dot(c, d) # matrix multiplication
f = np.sin(e)
g=b<c
a.sum()
a.min()
a.max()
