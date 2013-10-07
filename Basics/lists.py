a = ['spam', 'eggs', 100, 1234]
print a
print a[0]    
print a[2:4]
print a[-2]
print a[1:-1]
print 3*a[:3] + ['Boo!']

a[2] = a[2] + 23         # Lists are mutable!
a[0:2] = [1, 12]         # Replace items
a[0:2] = []              # Remove items (also try del a[0:2])
a[1:1] = ['urk', 'purk'] # Insert items
a.append('tjohoo!')      # Append items
a.insert(3, a)           # Insert a copy of a into a

print a
print a[3][2]            # Nested lists
print len(a)             # Number of elements in a
del a                    # Get rid of a

