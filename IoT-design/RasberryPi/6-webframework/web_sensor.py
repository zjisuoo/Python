from flask import Flask
import RPi.GPIO as IoPort
from dht_fn import sensor

IoPort.setmode(IoPort.BCM)
IoPort.setup(4, IoPort.OUT)

app = Flask(__name__)

@app.route("/lamp/<control>")
def control(control) :
    if control == "on" :
        IoPort.output(17, True)
    elif control == "off" :
        IoPort.output(17, False)
    return "Table lamp is now %s" % control

@app.route("/sensor")
def read_sensor()  :
    data = sensor()
    if data = None :
        return "None"
    # return "Sensor Read"
    return "Temp : %s Humidity : %s" % (data[0], data[1])

if __name__ == "__main__" :
    app.run('0.0.0.0')