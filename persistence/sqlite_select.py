import sqlite3 as lite

ita = ('ITA',)

con = lite.connect('sqlite.db')
c = con.cursor()
c.execute('SELECT * FROM PERSONS WHERE AFFILIATION=?', ita)
print c.fetchall()
con.commit()
c.close()
