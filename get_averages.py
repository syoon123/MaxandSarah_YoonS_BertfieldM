import sqlite3

db = sqlite3.connect("discobandit.db")
c = db.cursor()

cmd = "select name, mark from students, courses where students.id == courses.id"
sel =c.execute(cmd)

def generateDict():
    d = {}
    for record in sel:
        name = record[0]
        mark = record[1]
        if name in d:
            d[name].append(mark)
        else:
            d[name] = [mark]
    return d

def calculateAvg(list):
    s = 0
    ctr = 0
    for n in list:
        s += n
        ctr += 1
    return 1.0*s/ctr
            
def getAverages(dict):
    for student in dict:
        print "%s: %f" %(student, calculateAvg(dict[student]))

d = generateDict()
getAverages(d)

        

