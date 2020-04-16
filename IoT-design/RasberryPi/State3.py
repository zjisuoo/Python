import RPi.GPIO as IoPort 
import time

Port1 = 18
Port2 = 23

def State_1(Delay) : 
    IoPort.output(Port1, True) 
    IoPort.output(Port2, False) 
    time.sleep(Delay)

def State_2(Delay) :
    IoPort.output(Port1, True) 
    IoPort.output(Port2, True) 
    time.sleep(Delay)

def State_3(Delay) : 
    IoPort.output(Port1, False) 
    IoPort.output(Port2, True) 
    time.sleep(Delay)

def State_4(Delay) :
    IoPort.output(Port1, False)
    IoPort.output(Port2, False)
    time.sleep(Delay)

IoPort.setmode(IoPort.BCM)
IoPort.setup(Port1, IoPort.OUT) 
IoPort.setup(Port2, IoPort.OUT)  
time.sleep(0.4)

for I in range(0,10) : 
    State_1(0.4)
    State_2(0.4)
    State_3(0.4)
    State_4(0.4)