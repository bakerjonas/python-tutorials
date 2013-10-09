import sqlite3 as lite

lecturers = [('Jonas Juselius', 'jonas.juselius@uit.no', 'ITA'),
            ('Roy Dragseth', 'roy.dragseth@uit.no', 'ITA'),
            ('Dan Jonsson', 'dan.jonsson@uit.no', 'ITA')]
adm = ('Admin', 'noreply@uit.no', 'N/A')

with lite.connect('mydata.db') as con:
    c = con.cursor()
    c.execute('INSERT INTO persons VALUES(?, ?, ?)', adm)
    c.executemany('INSERT INTO persons VALUES(?, ?, ?)', lecturers)
