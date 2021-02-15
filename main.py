import hashlib
import json
from time import time

class Blockchain():
    def __init__(self) -> None:
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="The times 03/jan/2009 chancellor on brink for second bailout", proof=100)

    def new_block(self,proof, previous_hash=None):
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transactions=[]
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, receipient, amount):
        transaction = {
            'sender': sender,
            'recipient': receipient,
            'amount' : amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash =hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

bc = Blockchain()
t1 = bc.new_transaction('Satoshi','Chad','5 BTC')
t2 = bc.new_transaction('Chad', 'Grace','2 BTC')
bc.new_block(12345)

print("Blockchain: ", json.dumps(bc.chain, indent=4, sort_keys=True))