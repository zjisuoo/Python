from flask import Flask
import RPi.GPIO as IoPort

IoPort.setmode(IoPort.BCM)
IoPort.setup(17, IoPort.OUT)

app = Flask(__name__)

@app.route("/lamp/<control>")
def control(control) :
    if control == "on" :
        IoPort.output(17, True)
    elif control == "off" :
        IoPort.output(17, False)
    return "Table lamp is now %s" % control

if __name__ == "__main__" :
    app.run('0.0.0.0')