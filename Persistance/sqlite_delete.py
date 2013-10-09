import sqlite3 

con = sqlite3.connect('mydata.db')
c = con.cursor()
c.execute('DELETE FROM persons WHERE name = ?', ('Admin',))
con.commit()
con.close()
