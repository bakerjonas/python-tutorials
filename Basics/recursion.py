def oroborus(n, m=10):
    """Functions can be recursive!
    
    This function bites its own tail, over and over again.
    Then it spits it out again. 
    """
    k = 0
    if n < m:
        print 'Here we go again, round', n
        k = oroborus(n + 1)
    print "Unwinding", n
    return k + n

v = oroborus(5)
print v
