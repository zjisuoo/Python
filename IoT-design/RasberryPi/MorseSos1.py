import RPi.GPIO as IoPort
import time

Led = 18
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
print("- = 0.4 ddon")
print(". = 0.4 th")

try :
    while(True) :
        print("......")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(2.4)
        print("-")
        IoPort.output(Led, IoPort.HIGH)
        time.sleep(0.4)
        print(".")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(0.4)
        print("-")
        IoPort.output(Led, IoPort.HIGH)
        time.sleep(0.4)
        print(".")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(0.4)
        print("..")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(1.2)
        print("--")
        IoPort.output(Led, IoPort.HIGH)
        time.sleep(1.2)
        print(".")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(0.4)
        print("--")
        IoPort.output(Led, IoPort.HIGH)
        time.sleep(1.2)
        print(".")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(0.4)
        print("--")
        IoPort.output(Led, IoPort.HIGH)
        time.sleep(1.2)
        print("..")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(1.2)
        print("-")
        IoPort.output(Led, IoPort.HIGH)
        time.sleep(0.4)
        print(".")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(0.4)
        print(".")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(0.4)
        print("-")
        IoPort.output(Led, IoPort.HIGH)
        time.sleep(0.4)
        print(".")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(0.4)
        print("-")
        IoPort.output(Led, IoPort.HIGH)
        time.sleep(0.4)
        print("..")
        IoPort.output(Led, IoPort.LOW)
        time.sleep(1.2)

finally :
    print("IoPort cleanup")
    IoPort.cleanup()

