import sqlite3

conn=sqlite3.connect('face.db')
c=conn.cursor()

def create_table():
        c.execute("CREATE TABLE IF NOT EXISTS personInfo(person_id Integer Primary Key AutoIncrement,person_name Text,person_img BLOB)")
        #print("table created")

create_table()
