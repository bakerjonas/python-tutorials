import sqlite3 as lite

con = lite.connect('sqlite.db')
c = con.cursor()
c.execute('DROP TABLE PERSONS')
con.commit()
c.close()
