import sqlite3 as lite

name = 'Stian Bjørn Høgås'
con = lite.connect('sqlite.db')
c = con.cursor()
c.execute('DELETE FROM PERSONS WHERE NAME = ?', name,)
con.commit()
c.close()
