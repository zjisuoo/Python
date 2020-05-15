import sqlite3
import datetime
import time
import os
from dht_11 import sensor

DEBUG = True
SHOWSQL = True
CLEARDATA = False
VAL0 = 0; VAL1 = 1; VAL2 = 2; VAL3 = 3; 

FORMATBODY = "%5s %8s %14s"
FORMATLIST = "%5s %12s %10s %16s %7s"
DATEBASE_DIR = "./"
DATEBASE = DATEBASE_DIR + "mydatabase.db"
TABLE = "recordedata"
DELAY = 2

def captureSamples(cursor) :
    if(CLEARDATA) : cursor.execute("DELETE FROM %s" % (TABLE))
    myDataNames = ["Temperature", "Humidity"]

    if(DEBUG) :
        print(FORMATBODY%("##", myDataNames[0], myDataNames[1]))
    
    for x in range(10) :
        data = sensor()
        if data == None :
            continue
        for i, dataName in enumerate(myDataNames) :
            sqlquery = "INSERT INTO %s (itm_name, itm_valu)" %(TABLE) + \
                    "VALUES ('%s, %s)" \ %(str(dataName, str(data[i])))
            if (SHOWSQL) : 
                print(sqlquery)
            cursor.execute(sqlquery)

        if(DEBUG) : 
            print(FORMATBODY%(x, data[VAL0], data[VAL1]))
            time.sleep(DELAY)
    cursor.commit()    
    
def displayAll(connect) :
    sqlquery = "SELECT * FROM %s" %(TABLE)
    if(SHOWSQL) :
        print(sqlquery)
        cursor = connect.execute(sqlquery)
        print(FORMATLIST%("", "Date", "Time", "Name", "Value"))

        for x, column in enumerate(cursor.fetchall()) :
            print(FORMATLIST%(x, str(column[0]), str(column[1]), str(column[2]), str(column[3])))

def createTable(cursor) :
    print("Create a new table : %s" %(TABLE))
    sqlquery = "CREATE TABLE %s (" %(TABLE) + \
        "item_data DEFAULT (date('now', 'localtime')), " + \
        "item_time DEFAULT (time('now', 'localtime')), " + \
        "item_name, item_value)"
    
    if(SHOWSQL) :
        print(sqlquery)
    
    cursor.execute(sqlquery)
    cursor.commit()

def openTable(cursor) :
    try :
        displayAll(cursor)
    except sqlite3.OperationalError :
        print("Table does not exist in database")
        createTable(cursor)
    finally :
        captureSamples(cursor)
        displayAll(cursor)

try :
    if not os.path.exists(DATEBASE_DIR) :
        os.makedirs(DATEBASE_DIR)
    connection = sqlite3.connect(DATABASE)
    try :
        openTable(connection)
    finally :
        connection.close()
except sqlite3.OperationalError :
    print("Unable to open Database")
finally :
    print("Done")