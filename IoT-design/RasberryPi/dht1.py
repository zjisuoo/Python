from time import sleep
import adafruit_DHT

sensor = adafruit_DHT.DHT11

while True :
    humidity, temperature = adafruit_dht.read_retry(sensor, 12)

    if humidity is not None and temperature is not None :
        print("Temp = {0:0.1f}C  Humidity = {1:0.1f}%".format(temperature, humi dity))
    else :
        print("Failed to get reading. Try again!")
        
    sleep(2)