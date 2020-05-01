import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D4)

def sensor() :
    try :
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        
        if temperature_c == None or humidity == None :
            return None
        return temperature_c, humidity
    except RuntimeError  as error :
        print(error.args[0])