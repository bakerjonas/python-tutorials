class Cheese(object):
    def __init__(self, n = 10):
        self.nholes = n

    def __iter__(self):
        self.count = 0
        return self

    def next(self):
        print "Hey! Another hole!"
        self.count += 42
        if self.count > 42 * self.nholes: raise StopIteration
        return self.count

for i in Cheese(): print i
