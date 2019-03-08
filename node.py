import commands
from aes_cipher import AESCipher
from time import time

class Node:
	def __init__(self, ledger):
		self.bdaddr = self.get_local_bdaddr()
		
		try:
			index = ledger.index(self.bdaddr)
			ledger.remove(self.bdaddr)
			limit = len(ledger)
			self.ledger_count = index 
			if self.ledger_count >= limit:
				self.ledger_count = self.ledger_count%limit
		except ValueError:
			self.ledger_count = 0
		
		self.ledger = ledger
		self.cipher = AESCipher()
		self.key = "KEY"
		
		
	def get_local_bdaddr(self):
		_ , output = commands.getstatusoutput("hciconfig")
		return output.split("hci0:")[1].split("BD Address: ")[1].split(" ")[0] 
	
	def pull_from_ledger(self):
		limit = len(self.ledger)
		value = self.ledger[self.ledger_count]
		self.ledger_count+=1
		if self.ledger_count >= limit:
			self.ledger_count = self.ledger_count%limit
		return value

	def get_ledger(self):
		return self.cipher.encrypt(self.ledger, self.key)

	def get_consensus_packet(self):
		message = {
			"Source": self.bdaddr,
			"Chain": self.get_ledger(),
			"Timestamp": int(time())
		}
		return self.cipher.encrypt(self.ledger, self.key)
	
	def read_packet(self, packet):
		message = self.cipher.decrypt(packet, self.key)
		print(message)
