from bluetooth import *
import time

route = "B8:27:EB:F1:6C:F3"

while(True):
    sent = False
    while(not sent)
        try:
            client_socket=BluetoothSocket( RFCOMM )
            client_socket.connect((route, 3))
            client_socket.send("Hello World")
            print "Finished"
            client_socket.close()
            time.sleep(2)
            sent = True
        except Exception as e:
            print e
    
    
    server_socket=BluetoothSocket( RFCOMM )
    server_socket.bind(("", 3 ))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024)
    print "received [%s]" % data
    client_socket.close()
    server_socket.close()
