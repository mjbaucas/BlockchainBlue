from node import Node
import time
import socket
import os

node = Node()
record = open("message_records.txt", "w+")
while(True):
    # Reset variables
    sent = False
    trial = 0
    
    # Attempt to send packet to other device
    while(not sent and trial <= 3):
        try:
			route = node.pull_from_ledger()
			server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			server.bind((route, 32500))
			server.listen(1)
			connection, address = server.accept()
			packet = connection.recv(1024)
			data = node.read_packet(packet)
			print "received [{}]".format(data)
			print "{}".format(node.verify_ledger(data['Chain']))
			connection.send(node.get_consensus_packet())
			print "Message sent to {}".format(route)
			record.write("{} {} {} 1 \n".format(node.bdaddr, route, int(time.time())))
			sent = True
        except Exception as e:
			trial+=1
			time.sleep(1)
			record.write("{} {} {} 0 \n".format(node.bdaddr, route, int(time.time())))
			print e
    
    # Close sockets
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()
    server.shutdown(socket.SHUT_RDWR)
    server.close()
