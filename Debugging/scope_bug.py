def some_func():
    print "\nthis function just prints some stuff"
    print "to show how a loop works"


    outside_ctr = 0
    stop = 5
    for ctr in range(0, stop):
        print ctr, outside_ctr
        outside_ctr += incr

def do_loops():
    incr = 2
    some_func()

if __name__ == '__main__':
    do_loops()
