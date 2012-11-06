fd = file("Python-workshop-participants.rst", 'r')

participants = list()
for line in fd.readlines():
    if '@' in line:
        _, name, email, affiliation = map(str.strip, line.split(','))
        p = dict(name=name, email=email, affiliation=affiliation)
        participants.append(p)
        
    if 'pending' in line:
        break

for p in participants:
    if p['email'].endswith('uit.no'):
        print "name=%(name)25s email=%(email)20s affiliation=%(affiliation)20s" % p
