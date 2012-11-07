import shelve

print "Retrieving shelved lists."

variety = ['sweet', 'hot', 'sour']
shape = ['whole', 'spear', 'chip']
brand = ['Claussen', 'Heinz', 'Vlassic']

f = shelve.open('shelf.dat')
shape = f['shape']
brand = f['brand']
variety = f['variety']
print variety, shape, brand

f.close()