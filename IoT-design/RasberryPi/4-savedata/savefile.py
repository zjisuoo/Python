import time
import datetime
from dht_fn import sensor

DEBUG = True
FILE = True
VAL 0 = 0; VAL1 = 1; VAL2 = 2; VAL3 = 3 # Set data order
FORMATTHEADER = "/t %s /t %s /t %s"
FORMATBODY = "%d /t %s /t %f /t %f" 

if(FILE):f = open("data.log", 'w')

def timestamp() :
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def main() : 
    counter= 0
    header = (FORMATTHEADER%("Time", "Temperature", "Humidity"))
    if(DEBUG) : print(header)
    if(FILE) : f.write(header + "/n")
    while(1) :
        data = sensor()
        if data == None :
            continue
        counter += 1
        body = (FORMATBODY%(counter, timestamp(), data[0], data[1]))
        if(DEBUG) : print(body)
        if(FILE) : f.write(body + "/n")

try :
    main()
finally :
    f.close()