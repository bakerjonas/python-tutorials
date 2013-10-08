import csv
fd = file("Python-workshop-participants.rst", "r")
participants = list()
for line in fd.readlines():
    if '@' in line:
        _, name, email, affiliation = map(str.strip, line.split(','))
        p = dict(name=name, email=email, affiliation=affiliation)
        participants.append(p) 
    if 'pending' in line:
        break

from lxml.builder import E
from lxml import etree

participantelements = list()
for p in participants:
    element = E.participant(E.name(p["name"]),
                          E.email(p["email"]),
                          E.affiliation(p["affiliation"]))
    participantelements.append(element)

print etree.tostring(E.participants(*participantelements), pretty_print=True)

