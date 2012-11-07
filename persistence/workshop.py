# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, name, email, affiliation):
        self.name = name
        self.email = email
        self.affiliation = affiliation

    def asTuple(self):
        return self.name, self.email, self.affiliation

    def __str__(self):
        return  self.name + ', ' + \
                self.email + ', ' + \
                self.affiliation

class Workshop(object):
    def __init__(self, name, participants = None, header = None):
        self.name = name
        self.participants = participants or []
        self.header = header

    def printWorkshop(self):
        print self.name
        print '-'*len(self.name) + '\n'

        if not self.participants:
            print "No participants registered."

        if not self.header:
            print "No header defined."

        part = [participant.asTuple() for participant in self.participants]
        # Find max length of columns
        col_lengths = [max(len(word) for word in col) for col in zip(*part)]

        # Print header
        for h, l in zip(self.header, col_lengths):
            print "".join(h.ljust(l)) + '\t',
        print

        # Print participants
        i = 1
        for p in part:
            for s, l in zip(p, col_lengths):
                print "".join(s.ljust(l)) + '\t',
            print
        print '\n'
