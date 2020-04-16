import RPi.GPIO as IoPort
import time

def Sig_a(Port1, Port2, Delay) :
    IoPort.output(Port1, False)
    IoPort.output(Port2, True)
    time.sleep(Delay)
    IoPort.output(Port2, False)
    time.sleep(Delay)

def Sig_b(Port1, Port2, Delay) :
    IoPort.output(Port1, True)
    IoPort.output(Port2, True)
    time.sleep(Delay)
    IoPort.output(Port2, False)
    time.sleep(Delay)

def Sig_c(Port1, Port2, Delay) :
    IoPort.output(Port1, True)
    IoPort.output(Port2, True)
    time.sleep(Delay)
    IoPort.output(Port1, False)
    IoPort.output(Port2, False)
    time.sleep(Delay)

def Send_S(Port1, Port2) :
    Sig_c(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_a(Port1, Port2, 0.4)

def Send_O(Port1, Port2) :
    Sig_b(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_b(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_b(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_a(Port1, Port2, 0.4)

Led = 18
Clk = 23
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
IoPort.setup(Clk, IoPort.OUT)

Sig_a(Led, Clk, 0.4)
Sig_a(Led, Clk, 0.4)
Sig_a(Led, Clk, 0.4)
Send_S(Led, Clk)
Send_O(Led, Clk)
Send_S(Led, Clk)
Sig_a(Led, Clk, 0.4)
Sig_a(Led, Clk, 0.4)
