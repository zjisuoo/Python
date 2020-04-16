import RPi.GPIO as IoPort 
import time

def candle(Port, on, off) :
    global Count
    for i in range(0, Count) :
        IoPort.output(Port, True) 
        time.sleep(on) 
        IoPort.output(Port, False) 
        time.sleep(off)

def State1(Led) :
    for i in range(0, 40) :
        sub = i * 0.03 / 40
        candle(Led, 0.03 - sub, sub) 
        
def State2(Led) :
    for i in range(0, 40) : 
        sub = i * 0.03 / 40
        candle(Led, sub, 0.03 - sub) 

Led = 18
Count = 30 
IoPort.setmode(IoPort.BCM) 
IoPort.setup(Led, IoPort.OUT) 

while True :
    State1(Led) 
    State2(Led)