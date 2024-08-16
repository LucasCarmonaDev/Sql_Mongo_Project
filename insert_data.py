from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority")
db = client.bank

cliente_document = {
    "nome": "João",
    "contas": [
        {"numero": "12345"},
        {"numero": "67890"}
    ]
}
db.clientes.insert_one(cliente_document)
