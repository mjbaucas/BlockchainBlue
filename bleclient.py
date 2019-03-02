from bluetooth import *
import time

while(True):
    client_socket=BluetoothSocket( RFCOMM )
    client_socket.connect(("B8:27:EB:F1:6C:F3", 3))
    client_socket.send("Hello World")
    print "Finished"
    client_socket.close()
    time.sleep(5)
