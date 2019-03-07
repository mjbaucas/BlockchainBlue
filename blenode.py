from bluetooth import *
from node import Node
import time

ledger = [
	"B8:27:EB:F1:6C:F3",
	"B8:27:EB:B4:34:F1"
]

node = Node(ledger)

counter = 0
while(True):
    sent = False
    trial = 0
    while(not sent and trial <= 5):
        try:
            client_socket=BluetoothSocket( RFCOMM )
            client_socket.connect((node.pull_from_ledger(), 3))
            client_socket.send("Hello World")
            print "Finished"
            client_socket.close()
            sent = True
        except Exception as e:
            trial+=1
            time.sleep(3)
            print e
        counter+=1
    
    
    server_socket=BluetoothSocket( RFCOMM )
    server_socket.bind(("", 3 ))
    server_socket.listen(5)
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024)
    print "received [%s]" % data
    client_socket.close()
    server_socket.close()
    time.sleep(3)
