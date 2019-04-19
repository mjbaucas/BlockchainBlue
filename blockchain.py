import datetime
from block import Block

class Chain:
	def __init__(self):
		self.chain = [gen_genesis_block()]

	def gen_next_block(self, public_key, transactions):
		prev_block = self.chain[-1]
		index = prev_block.index + 1
		timestamp = datetime.datetime.now()
		data = transactions
		hashed_block = prev_block.gen_hashed_block()
		self.chain.append(Block(index, timestamp, data, hashed_block, public_key))
	
	def display_contents(self):
		for block in self.chain:
			block.disp_block_info()
	
	def output_ledger(self):
		main_transactions = []
		for block in self.chain:
			if block.index != 0:
				temp_transactions = block.get_block_transactions()
				for temp_transaction in temp_transactions:
					main_transactions.append(temp_transaction)
		return main_transactions

def gen_genesis_block():
	transaction = ["XX:XX:XX:XX:XX"]
	return Block(0, datetime.datetime.now(), transaction, "0", "0")

