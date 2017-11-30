
# Register nodes with each other

curl -X POST -H "Content-Type: application/json" -d '{
 "nodes": ["http://127.0.0.1:5124"]
}' "http://localhost:5123/nodes/register"

curl -X POST -H "Content-Type: application/json" -d '{
 "nodes": ["http://127.0.0.1:5123"]
}' "http://localhost:5124/nodes/register"

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5123/transactions/new"

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5124/transactions/new"

curl "http://localhost:5123/mine"
curl "http://localhost:5124/mine"

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5123/transactions/new"

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5123/transactions/new"

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5124/transactions/new"

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5124/transactions/new"
curl "http://localhost:5123/mine"
curl "http://localhost:5124/mine"

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5124/transactions/new"
curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5124/transactions/new"

curl "http://localhost:5124/mine"




curl "http://localhost:5123/nodes/resolve"
curl "http://localhost:5124/nodes/resolve"



