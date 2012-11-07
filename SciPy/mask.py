import numpy as np
import numpy.ma as ma

x = np.array([1, 2, 3, -1, 5])
print "Mean:", x.mean()
mx = ma.masked_array(x, mask=[0, 0, 0, 1, 0])
print "Masked array:", mx
print "Masked mean:", mx.mean()
y = np.zeros(5)
mask = x < y
print "Mask:", mask
mx = ma.masked_array(x, mask=mask)
print "Masked array:", mx
print "Masked mean:", mx.mean()
print "Masked array:", ma.masked_less(x, 3)

