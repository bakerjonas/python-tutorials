f = open('foo.txt', 'r')
print(f.readlines())

g = open('bar.txt', 'w')

f.seek(0) # Rewind the file
for i in f:
    l = i.strip().split()
    if len(l) > 0:
        print >> g, (l[2]) 
f.close()
g.close()

