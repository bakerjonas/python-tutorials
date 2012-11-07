import shelve

print "\n\nShelving lists."

variety = ['sweet', 'hot', 'sour']
shape = ['whole', 'spear', 'chip']
brand = ['Claussen', 'Heinz', 'Vlassic']

f = shelve.open('shelf.dat')

f['variety'] = variety
f['shape']  = shape
f['brand'] = brand

f.sync()
f.close()