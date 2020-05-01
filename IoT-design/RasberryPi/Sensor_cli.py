import time
import socket
from dht_fn import sensor
com_socket = socket.socket()
com_socket.connect(('192.168.1.2',20001))

while True :
    val = sensor()
    
    if val == None : 
        continue
    
    send_data = "Temp : {}C, Humid : {}%".format(val[0], val[1])
    print(send_data)
    com_socket.send(bytes(send_data,"UTF-8"))
    time.sleep(4.0)