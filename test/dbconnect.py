import sqlite3
import numpy as np
import cv2
import io


conn=sqlite3.connect('imagegal.db')
c=conn.cursor()

def create_Table():
    c.execute('CREATE TABLE IF NOT EXISTS test(id Integer Primary Key AutoIncrement,Description TEXT,Narray array,BGRarray array)')
    
def insert_Data(i,desc,narr,carr):
    c.execute('INSERT INTO test VALUES(?,?,?,?)',(i,desc,narr,carr))
    print("INSERTED")

def delete_Data():
    c.execute('DELETE FROM test')
    
def retrive_Data():
    c.execute('SELECT * FROM test ')
    rows=c.fetchall()
    for row in rows:
        print(row)

def adapt_array(arr):
    out=io.BytesIO()
    np.save(out,arr)
    out.seek(0)
    return np.load(out)

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)

img=cv2.imread('cdd.png')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

narr=np.asarray(img,dtype='int32')
carr=np.asarray(img1,dtype='int32')

sqlite3.register_adapter(np.ndarray,narr)
nar=np.arange(12).reshape(2,6)

# Converts TEXT to np.array when selecting
sqlite3.register_converter("array", convert_array)

sqlite3.register_adapter(np.ndarray,carr)
car=np.arange(12).reshape(2,6)
desc="its an umbrella"
#create_Table()
insert_Data(1,desc,narr,carr)

retrive_Data()
#delete_Data()
