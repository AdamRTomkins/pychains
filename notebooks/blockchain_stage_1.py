import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask

class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        
        # Create the genisis block
        self.new_block(previous_hash=1,proof=100)
        
    def new_block(self, proof, previous_hash=None):
        """
        Create a new block for the block chain
        
        :param proof <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of the previous Block
        :return <dict> New Block        
        """
        
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' :  time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        
        # reset the current list of transactions
        self.current_transactions = []
        
        self.chain.append(block)
        return block
        
    def new_transaction(self,sender,recipient,amount):
        """
        Create a new transaction to go into the next mined block.
        
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount <int> Amount to send
        :return <int> The index of the Block  that will hold this transaction
        """
        
        self.current_transactions.append(
            {   'sender': sender,
                'recipient' : recipient,
                'amount': amount
            }
        )
        
        return self.last_block['index'] + 1
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a Block
        
        :param block: <dict> Block
        :return <str>
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm
        - Find a number p' such that hash(pp') contains 4 leading zeros, where p is the previous block's p 
        - p is the previous proof, and p' is the new proof
        
        :param last_proof: <int>
        :return <int>
        """
        
        proof = 0
        while self.valid_proof(last_proof,proof) is False:
            proof += 1
            
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validate the proof, does hash(last_proof,proof) contain 4 leading zeros?
        
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current proof
        :return <bool> True if correct, False if not.
        """
        
        guess = ("%s%s"% (last_proof,proof)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
if __name__ == "__main__":
    
    from flask import Flask, jsonify, request
    import hashlib
    import json

    from time import time
    from uuid import uuid4

    from flask import Flask
    
    # Instantiate our Node
    app = Flask(__name__)

    # Generate a globally unique address for this node
    node_identifier = str(uuid4()).replace('-', '')

    # Instantiate the Blockchain
    blockchain = Blockchain()

    @app.route('/mine', methods=['GET'])
    def mine():
        # Run the proof of work algorithm to get the next proof
        last_block = blockchain.last_block
        last_proof = last_block['proof']
        proof = blockchain.proof_of_work(last_proof)

        # We must receive a reward for finding the proof.
        # The sender is "0" to signify that this node has mined a new coin.
        blockchain.new_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1,
        )

        # Forge the new block
        previous_hash = blockchain.hash(last_block)
        block = blockchain.new_block(proof,previous_hash)

        respose = {
            'messge': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],

        }

        return jsonify(response), 200

    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        print "accessed new transaction"
        values = request.get_json()

        print "validating request"
        # validate the required fields are in the json
        required = ['sender','recipient','amount']
        if not all(k in values for k in required):
            return 'Missing values in transaction', 400
        print "valided request"
        
        print "creating a transaction"
        # Create a new transaction
        index = blockchain.new_transaction(values['sender'],values['recipient'],values['amount'])
        print "created a transaction"

        response = {'message': 'Transaction will be added to Block %s' % index}

        return jsonify(response), 201


    @app.route('/chain', methods=['GET'])
    def full_chain():
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain),
        }
        return jsonify(response), 200

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5123)


