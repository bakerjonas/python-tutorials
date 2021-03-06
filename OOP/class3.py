class Foobar:
    def __init__(self, x):
        self.foo = x

    def __len__(self):
        return 42

    def __getitem__(self, key):
        if key.lower() != "oof":
            raise IndexError('We only accept oof:s!')
        return self.foo

    def __getattr__(self, key):
        if key.lower() != "foo":
            raise KeyError('We only have a foo!')
        return self.foo

f = Foobar(-42)
print len(f), f['oOf']
print f.foo
print f['foo']
