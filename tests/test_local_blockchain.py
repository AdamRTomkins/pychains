from blockchain import *

node_identifier = str(uuid4()).replace('-', '')

sender = hashlib.sha256('me')
recipient = hashlib.sha256('you')
amount = 1

bc =  Blockchain()
bc.new_transaction(sender,recipient,amount)

print bc.current_transactions
print bc.chain

last_block = bc.last_block
last_proof = last_block['proof']
proof = bc.proof_of_work(last_proof)

# We must receive a reward for finding the proof.
# The sender is "0" to signify that this node has mined a new coin.
bc.new_transaction(
    sender="0",
    recipient=node_identifier,
    amount=1,
)

# Forge the new block
previous_hash = bc.hash(last_block)
block = bc.new_block(proof,previous_hash)

print bc.current_transactions
print bc.chain