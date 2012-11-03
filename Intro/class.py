class Foobar:
    bar = True
    
    def __init__(self, x):
        self.foo = x

    def __str__(self):
        return 'Foobar is %d %r.' % (self.foo, self.bar)

    def double(self):
        self.foo *= 2
        return self.foo
