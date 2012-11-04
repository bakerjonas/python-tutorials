t = 1, 2, 'hello!'      # t = (1, 2, 'hello!')
print t
print t[0]

u = t, (1, 2, 3, 4, 5)  # Tuples may be nested:
t[0] = 88888            # Tuples are immutable
v = ([1, 2], [3, 2])    # but they can contain mutable objects

empty = ()
singlton = 'foo', 

x, y, z = t             # Sequence unpacking

s = set([4, 2, 4, 2, 'hej', 'hej'])
print s                 # Sets contain only unique elemetns

