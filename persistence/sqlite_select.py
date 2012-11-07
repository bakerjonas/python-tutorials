import sqlite3 as lite

ita = ('ITA',)

con = lite.connect('sqlite.db')
c = con.cursor()
c.execute('SELECT COUNT(*) FROM persons WHERE affiliation=? ORDER BY name', ita)
print c.fetchone()
c.execute('SELECT * FROM persons WHERE affiliation=? ORDER BY name', ita)
print c.fetchall()
con.commit()
c.close()
