from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority")
db = client.bank

cliente = db.clientes.find_one({"nome": "João"})
print(cliente)
