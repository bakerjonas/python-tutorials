import sqlite3 as lite


class DbTest(object):
    def __init__(self, name):
        self.name = name

    def createTables(self):
        con = lite.connect(self.name)
        c = con.cursor()
        c.execute('''CREATE TABLE persons
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, affiliation TEXT)''')
        con.commit()
        c.close()

    def insertValue(self):
        stian = ('Stian Bjørn Høgås', 'stian.hogas@uit.no', 'ITA')
        con = lite.connect(self.name)
        c = con.cursor()
        c.execute('INSERT INTO PERSONS VALUES(?, ?, ?)', stian)
        con.commit()
        c.close()

    def deleteValue(self):
        con = lite.connect(self.name)
        name = 'Stian Bjørn Høgås'
        c = con.cursor()
        c.execute('DELETE FROM PERSONS WHERE NAME = ?', name,)
        con.commit()
        c.close()


    def insertValues(self, cars):
        lecturers  = [('Jonas Juselius', 'jonas.juseliur@uit.no', 'ITA'), ('Roy Dragseth', 'roy.dragseth@uit.no', 'ITA'),
                     ('Lars Ailo Bongo', 'larseb@cs.uit.no', 'IFI'), ('Stian Bjørn Høgås', 'stian.hogas@uit.no', 'ITA')]

        con = lite.connect(self.name)
        c = con.cursor()
        c.executemany('INSERT INTO PERSONS VALUES(?, ?, ?)', lecturers)
        con.commit()
        c.close()


