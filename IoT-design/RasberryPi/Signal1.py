import RPi.GPIO as IoPort
import time

def State_A(Dly) :
    IoPort.output(SigA, False) 
    IoPort.output(SigB, False) 
    time.sleep(Dly)

def State_B(Dly) : 
    IoPort.output(SigA, False) 
    IoPort.output(SigB, True) 
    time.sleep(Dly)

def State_C(Dly) : 
    IoPort.output(SigA, True) 
    IoPort.output(SigB, False) 
    time.sleep(Dly)

def State_D(Dly) : 
    IoPort.output(SigA, True) 
    IoPort.output(SigB, True) 
    time.sleep(Dly)

SigA = 18
SigB = 23
IoPort.setmode(IoPort.BCM)
IoPort.setup(SigA, IoPort.OUT) 
IoPort.setup(SigB, IoPort.OUT) 
State_A(0.4)
State_C(0.4)
State_D(0.4)
State_B(0.4)
State_A(0.4)
State_C(1.4)
State_D(1.0)
State_B(0.2)
State_A(1.8)