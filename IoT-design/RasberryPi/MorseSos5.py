import RPi.GPIO as IoPort 
import time

def Sig_a() :
    IoPort.output(Led, False) 
    IoPort.output(Clk, True) 
    time.sleep(tmin) 
    IoPort.output(Clk, False) 
    time.sleep(tmin)

def Sig_b() : 
    IoPort.output(Led, True) 
    IoPort.output(Clk, True) 
    time.sleep(tmin) 
    IoPort.output(Clk, False) 
    time.sleep(tmin)

def ton() : 
    Sig_b() 
    Sig_a()

def thu() : 
    Sig_b() 
    Sig_b() 
    ton()

def dly() : 
    Sig_a() 
    Sig_a()

def Send_S() : 
    ton()
    ton()
    ton()

def Send_O() :
    thu() 
    thu() 
    thu()

Led = 18
Clk = 23
tmin = 0.2
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
IoPort.setup(Clk, IoPort.OUT) 
dly()
dly()
dly()
Send_S()
dly()
Send_O()
dly()
Send_S()
dly()
dly() 
dly()
