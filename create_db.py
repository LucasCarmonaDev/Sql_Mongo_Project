from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Cliente, Conta

engine = create_engine('sqlite:///bank.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Inserindo dados
cliente1 = Cliente(nome="João")
conta1 = Conta(numero="12345", cliente=cliente1)
session.add(cliente1)
session.add(conta1)
session.commit()
