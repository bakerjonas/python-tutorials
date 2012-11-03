f = open('foo.txt', 'w')
for i in range(5):
    print >> f, ("   Line number %d  " % i)
