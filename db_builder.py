import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

fObj = open("peeps.csv") 
d1=csv.DictReader(fObj)

gObj = open("courses.csv")
d2=csv.DictReader(gObj)

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

def gts(dict):
    for k in dict:
        ret = "'" + k['name'] + "'" +  "," + "'"+ k['id']+ "'"
        q = "INSERT INTO students VALUES (" + ret + ")"
        c.execute(q)

q = "CREATE TABLE students (name TEXT, id INTEGER)"
c.execute(q)    #run SQL query
gts(d1)

def gtc(dict):
    for k in dict:
        ret = "INSERT INTO courses VALUES(" + "'" +  k['code'] + "'" + "," + "'"  + k['mark'] + "'"+ "," + "'" + k['id'] + "'" + ")"
        c.execute(ret)

q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)
gtc(d2)


#==========================================================
db.commit() #save changes
db.close()  #close database


