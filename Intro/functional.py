a = [ '42', '33', '99', '1', '0']
b = map(float, a)
print b

def foo(x, y):
    print "  *reducing:", x, y
    return x + y

print "filter:", filter(lambda x: x < 40, b)
print "reduce:", reduce(foo, b)
print "sum:", sum(b)
print "any and all:", any(b), all(b)
