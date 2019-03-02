from bluetooth import *
import time

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

while(True):
    client_socket.connect(("B8:27:EB:F1:6C:F3", 3))
    client_socket.send("Hello World")
    print "Finished"
    client_socket.close()

