tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel
print tel['jack']

del tel['sape']
tel['irv'] = 4127
print tel

print tel.keys()
if 'guido' in tel: print "Hi there!"
for i in tel: print "Hello {}!".format(i)
