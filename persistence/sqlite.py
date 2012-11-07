# -*- coding: utf-8 -*-
import sqlite3 as sqlite
from convenience import WorkshopParser




if __name__ == "__main__":
    conn = sqlite.connect(":memory:")
    c = conn.cursor()


    c.execute("create table point (point str)")
    c.execute("insert into point values(?)", (p,))
    c.execute("select * from point")
    print c.fetchone()[0]
    c.close()
    conn.close()



#    sqlite.register_adapter(Point, Point.adapt)
#    sqlite.register_converter("Point", Point.convert)
#    useDecltypes(p)