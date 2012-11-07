# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3 as lite

name = ('Stian Bjørn Høgås',)
con = lite.connect('sqlite.db')
c = con.cursor()
c.execute('DELETE FROM persons WHERE name = ?', name)
con.commit()
c.close()
