from scipy import misc, ndimage
import matplotlib.pyplot as plt
import numpy as np

lena = misc.lena()
misc.imsave('lena.png', lena) 

plt.imshow(lena, cmap=plt.cm.gray)
plt.show()

lena = np.flipud(lena[150:350, 150:350])
lena = ndimage.rotate(lena, 45)
lena = ndimage.gaussian_filter(lena, 3)
plt.imshow(lena, cmap=plt.cm.gray)
plt.show()
