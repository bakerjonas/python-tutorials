import cPickle as pickle

print "Pickling lists."

variety = ['sweet', 'hot', 'sour']
shape = ['whole', 'spear', 'chip']
brand = ['Claussen', 'Heinz', 'Vlassic']

with open('pickles.dat', 'w') as f:
    pickle.dump(variety, f)
    pickle.dump(shape, f)
    pickle.dump(brand, f)
