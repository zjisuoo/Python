import RPi.GPIO as IoPort
import time

Led = 18
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)

try :
    while(True) :
        print("LED ON")
        IoPort.output(Led, IoPort.HIGH)
        time.sleep(2)
        print("LED OFF")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(2)

finally :
    print("IoPort cleanup")
    IoPort.cleanup()

