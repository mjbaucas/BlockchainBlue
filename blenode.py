from bluetooth import *
from node import Node
import time

ledger = [
	"B8:27:EB:9F:A5:AC",
	"B8:27:EB:8C:3E:7C",
    "B8:27:EB:F1:6C:F3",
    "B8:27:EB:13:01:59"
]

node = Node(ledger)

while(True):
    sent = False
    trial = 0
    
    while(not sent and trial <= 5):
        try:
            route = node.pull_from_ledger()
            client_socket=BluetoothSocket( RFCOMM )
            client_socket.connect((route, 3))
            client_socket.send(node.get_consensus_packet())
            print "Message sent to {}".format(route)
            client_socket.close()
            sent = True
        except Exception as e:
            trial+=1
            time.sleep(2)
            print e
    
    
    server_socket=BluetoothSocket( RFCOMM )
    server_socket.bind(("", 3 ))
    server_socket.listen(8)
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024)
    print "received [%s]" % node.read_packet(data)
    client_socket.close()
    server_socket.close()
