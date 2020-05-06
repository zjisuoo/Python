import socket

com_socket = socket.socket()
com_socket.bind(('192.168.219.103', 20000))
com_socket.listen(10)
conection, address = com_socket.accept()
print(address, "Connected.......")

while True :
    print(connection.recv(4096).decode("UTF-8"))
    send_data = input("Reply : ")
    connection.send(bytes(send_data, "UTF-8"))