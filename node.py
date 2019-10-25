import commands
import ast 
import hashlib
from time import time

from aes_cipher import AESCipher
from blockchain import Chain

# Temporary BLE Ledger
init_ledger = [
	"B8:27:EB:CA:80:6C",
	"B8:27:EB:13:01:59",
	"B8:27:EB:1B:F2:FC",
	"B8:27:EB:8C:3E:7C"
]

# Temporary WiFi Ledger
init_ledger = [
	"10.11.151.141"
]

class Node:
	# Initialization
	def __init__(self):
		#self.bdaddr = self.get_local_bdaddr()
		self.bdaddr = self.get_local_ipaddr()
		
		self.base_ledger = Chain()
		self.base_ledger.gen_next_block(hashlib.sha256("NodeAddressBlock1".encode()).digest(), init_ledger)
		
		# Set ledger count to position of local address in current ledger
		ledger = self.base_ledger.output_ledger()
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
	
	# Get IP address from device
	def get_local_ipaddr(self):
		return commands.getoutput('hostname -I')
	
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
		sha.update(str(self.base_ledger))
		return sha.hexdigest()
		#sha.update((str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash)).encode('utf-8'))
	
	# Verify ledger
	def verify_ledger(self, hashed_ledger):
		hashed_ledger = self.get_ledger()
		return hashed_ledger == hashlib.sha256(str(self.base_ledger)).hexdigest()

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
