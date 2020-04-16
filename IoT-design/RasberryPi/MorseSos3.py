import RPi.GPIO as IoPort
import time

def LedOn(Port, Delay) :
    IoPort.output(Port, True)
    time.sleep(Delay)

def LedOff(Port, Delay) :
    IoPort.output(Port, False)
    time.sleep(Delay)

def Send_S() :
    LedOn(Led, 0.4)
    LedOff(Led, 0.4)
    LedOn(Led, 0.4)
    LedOff(Led, 0.4)
    LedOn(Led, 0.4)
    LedOff(Led, 1.2)

def Send_O() :
    LedOn(Led, 1.2)
    LedOff(Led, 0.4)
    LedOn(Led, 1.2)
    LedOff(Led, 0.4)
    LedOn(Led, 1.2)
    LedOff(Led, 1.2)

Led = 18
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)

LedOff(Led, 2.4)
Send_S()
Send_O()
Send_S()