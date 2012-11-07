import sqlite3 as lite
con = lite.connect('sqlite.db')
c = con.cursor()
c.execute('''CREATE TABLE persons 
    (name TEXT, email TEXT, affiliation TEXT)''')
con.commit()
c.close()

