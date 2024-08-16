from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Cliente, Conta

engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
session = Session()

clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"Cliente: {cliente.nome}, Contas: {[conta.numero for conta in cliente.contas]}")
