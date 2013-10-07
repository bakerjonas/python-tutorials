with open('foo.txt', 'r') as f:
    lines = f.readlines()
    print lines

with open('foo.txt', 'r') as f:
    for i in f:
        l = i.strip().split()
        if len(l) > 3:
            print l[2]
    f.seek(0) # Rewind the file
    print f.readline()
