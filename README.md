# Projeto de Integração com Bancos de Dados Relacional e NoSQL

## Descrição

Este projeto foi desenvolvido como parte do desafio prático da DIO. Ele implementa uma integração com um banco de dados relacional utilizando SQLAlchemy e um banco de dados NoSQL utilizando Pymongo.

## Estrutura do Projeto

- `relational_db/`: Contém o código relacionado ao banco de dados relacional (SQLite).
  - `create_db.py`: Script para criar e popular o banco de dados.
  - `models.py`: Definição das classes do SQLAlchemy que representam as tabelas do banco de dados.
  - `queries.py`: Script contendo exemplos de consultas ao banco de dados.

- `nosql_db/`: Contém o código relacionado ao banco de dados NoSQL (MongoDB).
  - `insert_data.py`: Script para inserir dados no MongoDB Atlas.
  - `queries.py`: Script contendo exemplos de consultas ao banco de dados NoSQL.

## Configuração e Execução

### Banco de Dados Relacional (SQLite)

1. **Instalar dependências:**
   ```bash
   pip install sqlalchemy
2. **Criar e popular o banco de dados:**
   ```bash
   python relational_db/create_db.py
3. **Executar consultas:**
   ```bash
   python relational_db/queries.py

### Banco de Dados NoSQL (MongoDB)

1.**Instalar dependências:**
   ```bash
  pip install pymongo
2.**Configurar conexão com MongoDB Atlas:**
   ```bash
   Edite o arquivo nosql_db/insert_data.py e substitua <username> e <password> pelas suas credenciais do MongoDB Atlas.
3.**Inserir dados no MongoDB:**
   ```bash
   python nosql_db/insert_data.py
4.**Executar consultas:**
   ```bash
   python nosql_db/queries.py


### 2. Código Fonte

#### `relational_db/models.py`

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship("Cliente", back_populates="contas")





