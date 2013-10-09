import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

map = Basemap(llcrnrlat=50.0, urcrnrlat=80.0,
         llcrnrlon=0.0, urcrnrlon=30.0,
         resolution='l',area_thresh=10.,projection='lcc',
         lat_0=66.0,
         lon_0=15.0)

map.drawcoastlines()
map.fillcontinents(color='grey')
map.drawcountries()
map.drawmeridians(np.arange(0.0, 30.0, 10), labels=[0,0,0,1])
map.drawparallels(np.arange(50.0, 90.0, 4), labels=[1,0,0,0])

nlats = 50; nlons = 50; delta = 0.5*np.pi/(nlons-1)
lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
lons = (delta*np.indices((nlats,nlons))[1,:,:])
wave = 0.75*(np.sin(8.*lats)**8*np.cos(12.*lons))
mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)

# compute native map projection coordinates of lat/lon grid.
x, y = map(lons*180./np.pi, lats*180./np.pi)
cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
plt.title('contour lines over filled continent background')
plt.show()
