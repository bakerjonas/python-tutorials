import sqlite3 

con = sqlite3.connect('mydata.db')
c = con.cursor()
c.execute('''SELECT COUNT(*) FROM persons 
        WHERE affiliation=? ORDER BY name''', ('ITA',))
print c.fetchone()
c.execute('''SELECT * FROM persons 
    WHERE affiliation=? ORDER BY name''', ('ITA',))
for i in c.fetchall(): print i
con.commit()
con.close()
