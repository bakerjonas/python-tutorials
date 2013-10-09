tel = {'jonas': 4098, 'roy': 4139}
tel['dan'] = 4127
print tel
print tel['jonas']

del tel['roy']
tel['espen'] = 4127
print tel

print tel.keys()
if 'jonas' in tel: print "Hi there!"
for i in tel: 
    print "Hello {0}! Your number is {1}".format(i.capitalize(), tel[i])
