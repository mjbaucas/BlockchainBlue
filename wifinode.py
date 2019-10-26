from node import Node
import time
import socket
import os

node = Node()
record = open("message_records.txt", "w+")
while(True):
    # Reset variables
    sent = False
    bound = False
    send_trial = 0
    bound_trial = 0
    
    
    # Attempt to send packet to other device
    while(not sent and send_trial <= 3):
        try:
            route = node.pull_from_ledger()
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((route, 32500))
            client.send(node.get_consensus_packet())
            print "Message sent to {}".format(route)
            record.write("{} {} {} 1 \n".format(node.bdaddr, route, int(time.time())))
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            sent = True
        except Exception as e:
			send_trial+=1
			time.sleep(1)
			record.write("{} {} {} 0 \n".format(node.bdaddr, route, int(time.time())))
			print e
    
    # Wait for packet from other device
    while(not bound and bound_trial <= 3):
        try: 
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("", 32500))
            server.listen(5)
            connection, address = server.accept()
            packet = connection.recv(1024)
            data = node.read_packet(packet)
            print "received [{}]".format(data)
            print "{}".format(node.verify_ledger(data['Chain']))
            server.shutdown(socket.SHUT_RDWR)
            server.close()
            bound = True		
        except Exception as e:
            bound_trial+=1
            time.sleep(1)
            record.write("{} {} {} 0 \n".format(node.bdaddr, address, int(time.time())))
            print e
            
    # Close sockets
    connection.close()
    client.close()
    server.close()
