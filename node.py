import commands
import ast 
import hashlib
from time import time

from aes_cipher import AESCipher


class Node:
	# Initialization
	def __init__(self, ledger):
		self.bdaddr = self.get_local_bdaddr()
		
		# Set ledger count to position of local address in current ledger
		try:
			index = ledger.index(self.bdaddr)
			ledger.remove(self.bdaddr)
			limit = len(ledger)
			self.ledger_count = index 
			if self.ledger_count >= limit:
				self.ledger_count = self.ledger_count%limit
		except ValueError:
			# If local address was not found in ledger, set count to 0 >> TEMPORARY >> Unrecognized devices should not be allowed access to the loop
			self.ledger_count = 0
		
		self.ledger = ledger
		self.cipher = AESCipher()
		self.key = "KEY"
	
	# Get Bluetooth MAC address from device		
	def get_local_bdaddr(self):
		_ , output = commands.getstatusoutput("hciconfig")
		return output.split("hci0:")[1].split("BD Address: ")[1].split(" ")[0] 
	
	# Pull an address from the ledger
	def pull_from_ledger(self):
		limit = len(self.ledger)
		value = self.ledger[self.ledger_count]
		self.ledger_count+=1
		if self.ledger_count >= limit:
			self.ledger_count = self.ledger_count%limit
		return value
    
    # Get encrypted version of ledger
	def get_ledger(self):
		sha = hashlib.sha256()
		sha.update(str(self.ledger))
		return sha.hexdigest()
		#sha.update((str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash)).encode('utf-8'))
	
	# Verify ledger
	def verify_ledger(self, hashed_ledger):
		return hashed_ledger == hashlib.sha256(str(self.ledger)).hexdigest()

	# Create consensus packet
	def get_consensus_packet(self):
		message = {
			"Source": self.bdaddr,
			"Chain": self.get_ledger(),
			"Timestamp": int(time())
		}
		return self.cipher.encrypt(message, self.key)
	
	# Read packet
	def read_packet(self, packet):
		dict_str = self.cipher.decrypt(packet, self.key)
		return ast.literal_eval(dict_str)
