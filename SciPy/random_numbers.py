a = np.random.rand(10,10)
print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype.name)
print(a)
print(a[3, 4])
print(a[1, :])
print(a[0:4, 6:9])

for row in a:
    print(row)

for i in np.nditer(a):
    print(i)
  

