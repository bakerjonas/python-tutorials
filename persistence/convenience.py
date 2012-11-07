# -*- coding: utf-8 -*-

from workshop import Workshop, Person

def parseWorkshop(file_name = 'Python-workshop-participants.rst'):
    workshops = []

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                if line.startswith('.. csv-table'):
                    w_name = line[line.rindex(':')+1:].strip()
                    workshop = Workshop(w_name)
                    workshops.append(workshop)
                    continue

                if line.startswith(':header'):
                    headers = line[line.rindex(':')+1:].split(',')
                    workshop.header = map(str.strip, headers[1:])
                    continue

                if line[0].isdigit():
                    _, name, email, affiliation = map(str.strip, line.split(','))
                    workshop.participants.append(Person(name, email, affiliation))

    return workshops
