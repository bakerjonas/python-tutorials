class Foobar:
    def __init__(self, x):
        self.foo = x

    def double(self):
        self.foo *= 2
        return self.foo

foo = Foobar(42)
bar = Foobar("hey!")
print foo.foo, bar.foo
print foo.double(), bar.double()
print foo.foo, bar.foo
