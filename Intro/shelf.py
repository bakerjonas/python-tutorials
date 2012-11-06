import shelve

d = shelve.open("shelf.dbm") 

d['mother'] = 'hamster' 
d['father'] = 'elderberry' 
d['stuff'] = [1, 2, 75, 6, 7]

stuff = d['stuff']
print stuff
del d['stuff']
d.close()
