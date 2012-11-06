def oroborus(n, m=10):
    k = 0
    if n < m:
        print 'Here we go again, round', n
        k = oroborus(m + 1)
    print "Unwinding", n
    return k + n

if __name__ == '__main__':
    oroborus(5)