from bluetooth import *
import time

route = "B8:27:EB:B4:34:F1"

while(True):
    sent = False
    trial = 0
    while(not sent or trial <= 10):
        try:
            client_socket=BluetoothSocket( RFCOMM )
            client_socket.connect((route, 3))
            client_socket.send("Hello World")
            print "Finished"
            client_socket.close()
            sent = True
        except Exception as e:
            trial+=1
            time.sleep(2)
            print e
    
    
    server_socket=BluetoothSocket( RFCOMM )
    server_socket.bind(("", 3 ))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024)
    print "received [%s]" % data
    client_socket.close()
    server_socket.close()
