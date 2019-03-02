from bluetooth import *
import time

server_socket=BluetoothSocket( RFCOMM )

server_socket.bind(("", 3 ))

while(True):
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024)

    print "received [%s]" % data
    client_socket.close()
    time.sleep(3)

server_socket.close()
