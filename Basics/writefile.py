f = open('foo.txt', 'w')
f.write("Hello world?\n\n")

for i in range(5):
    print >> f, ("   Line number %d  " % i)

f.close()
