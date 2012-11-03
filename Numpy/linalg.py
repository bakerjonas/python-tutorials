from numpy import linalg
a = np.cos(np.arange(9).reshape(3,3))
linalg.det(a)
linalg.inv(a)
linalg.eig(a)
linalg.norm(a)
linalg.svd(a)

i = np.arange(3)
a[i,i] += 2
linalg.cholesky(a)
