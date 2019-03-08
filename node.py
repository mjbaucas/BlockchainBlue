import commands


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

