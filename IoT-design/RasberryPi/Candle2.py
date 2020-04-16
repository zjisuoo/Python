import RPi.GPIO as IoPort 
import time

def candle(Port, on, off) :
    global Count
    for i in range(0, Count) :
        IoPort.output(Port, True) 
        time.sleep(on) 
        IoPort.output(Port, False) 
        time.sleep(off)

Led=18 
IoPort.setmode(IoPort.BCM) 
IoPort.setup(Led, IoPort.OUT) 

for i in range(0, 40) :
    Count = 10 + I
    sub = i * 0.0005 
    candle(Led, 0.02 - sub, 0.01)