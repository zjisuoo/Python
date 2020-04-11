import RPi.GPIO as IoPort
import time

IoPort.setmode(IoPort.BCM)

IoPort.setup(18, IoPort.OUT)


try :
    while(True) :
        print("LED ON")
        IoPort.output(18, IoPort.HIGH)
        time.sleep(2)
        print("LED OFF")
        IoPort.output(18, IoPort.LOW)
        time.sleep(2)

finally :
    print("IoPort cleanup")
    IoPort.cleanup()


    