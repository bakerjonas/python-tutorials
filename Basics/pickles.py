import pickle

with open("bar.dat", 'w') as f:
    pickle.dump(range(10), f)
    pickle.dump("foo", f)

with open("bar.dat", 'r') as f:
    first = pickle.load(f)
    second = pickle.load(f)

print first
print second
