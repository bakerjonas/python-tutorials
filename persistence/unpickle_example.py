import cPickle as pickle

print "\n\nUnickling lists."

with open('pickles.dat', 'r') as f:
    variety = pickle.load(f)
    shape = pickle.load(f)
    brand = pickle.load(f)

print variety, shape, brand
