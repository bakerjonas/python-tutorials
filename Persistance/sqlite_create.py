import sqlite3  

con = sqlite3.connect('mydata.db')
c = con.cursor()
c.execute('''CREATE TABLE persons (name TEXT, email TEXT, affiliation TEXT)''')
con.commit()
con.close()

