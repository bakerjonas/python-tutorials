class Foobar:
    bar = True
    
    def __init__(self, x):
        self.foo = x

    def __str__(self):
        return 'Foobar is {0} / {1}.'.format(self.foo, self.bar)

    def double(self):
        self.foo *= 2
        return self.foo

a = Foobar(1)
b = Foobar(42)
print "a -> {0}\nb -> {1}".format(a, b) # invokes __str__()
print b.double() 
Foobar.bar = False                      # set global class variable
print "a -> {0}\nb -> {1}".format(a, b) # invokes __str__()
