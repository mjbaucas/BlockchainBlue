import commands


class Node:
	def __init__(self, ledger):
		self.bdaddr = self.get_local_bdaddr()
		self.ledge_count = 0
		
		try:
			ledger.remove(self.bdaddr)
		except ValueError:
			pass
		
		self.ledger = ledger
		
	def get_local_bdaddr(self):
		_ , output = commands.getstatusoutput("hciconfig")
		return output.split("hci0:")[1].split("BD Address: ")[1].split(" ")[0] 
	
	def pull_from_ledger(self):
		limit = len(self.ledger)
		self.ledge_count+=1
		if self.ledge_count >= limit:
			self.ledge_count = self.ledge_count%limit
		return self.ledger[self.ledge_count]

