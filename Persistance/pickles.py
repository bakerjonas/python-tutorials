import pickle
import numpy as np

with open("bar.dat", 'w') as f:
    pickle.dump("foo", f)
    pickle.dump(np.random.rand(5,5), f)

with open("bar.dat", 'r') as f:
    first = pickle.load(f)
    second = pickle.load(f)

print first
print second
