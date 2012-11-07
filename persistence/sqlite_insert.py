# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3 as lite

stian = ('Stian Bjørn Høgås', 'stian.hogas@uit.no', 'ITA')
lecturers  = [('Jonas Juselius', 'jonas.juseliur@uit.no', 'ITA'), ('Roy Dragseth', 'roy.dragseth@uit.no', 'ITA'),
              ('Lars Ailo Bongo', 'larseb@cs.uit.no', 'IFI')]

con = lite.connect('sqlite.db')
c = con.cursor()
c.execute('INSERT INTO PERSONS VALUES(?, ?, ?)', stian)
c.executemany('INSERT INTO PERSONS VALUES(?, ?, ?)', lecturers)
con.commit()
c.close()
