from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("00:12:D2:5A:BD:E4", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()
