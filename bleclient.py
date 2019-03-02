from bluetooth import *
import time

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )
client_socket.connect(("B8:27:EB:F1:6C:F3", 3))

while(True):
    client_socket.send("Hello World")
    print "Finished"
    time.sleep(3)

client_socket.close()
