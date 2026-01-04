import time
import hashlib

class Block:
    def __init__(self, index, nonce, prev_hash, data, timestamp=None):
        self.index = index
        self.nonce = nonce
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def calculate_hash(self):
        block_string = "{}{}{}{}{}".format(self.index,self.nonce,self.prev_hash,self.data,self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest
    
    def __repr__(self):
        return "{}-{}-{}-{}-{}".format(self.index,self.nonce,self.prev_hash,self.data,self.timestamp)

class BlockChain:
    def __init__(self):
        self.chain=[]
        self.current_data = []
        self.participants = set()
        self.construct_first()

    def construct_first(self):
        self.construct(nonce = 0,prev_hash = 0)
    
    def construct(self,nonce,prev_hash):
        block = Block(
            index = len(self.chain),
            nonce = nonce,
            prev_hash=prev_hash,
            data = self.current_data
        )
        self.current_data = []

        self.chain.append(block)
        return block
    
    @staticmethod
    def validity(block,prev_block):
        if prev_block.index + 1 != block.index:
            return False
        elif prev_block.calculate_hash != block.prev_hash:
            return False
        elif not BlockChain.verifying_proof(block.nonce,prev_block.nonce):
            return False
        elif block.timestamp <= prev_block.timestamp:
            return False

        return True
    
    def add_data(self,sender,recipent,quantity):
        self.current_data.append(
            {
                "sender" : sender,"recipent":recipent,"quantity":quantity
            }
        )
    
    @staticmethod
    def proof_of_work(last_nonce):
        req_nonce = 0
        while BlockChain.verifying_proof(req_nonce,last_nonce) == False:
            req_nonce+=1

        return req_nonce
    
    @staticmethod
    def verifying_proof(nonce,last_nonce):
        guess = f'{nonce}{last_nonce}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    @property
    def latest_block(self):
        return self.chain[-1]
    
    def create_node(self, address):
        self.nodes.add(address)
    
