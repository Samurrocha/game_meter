# app/database.py
from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env (caso necessário)
load_dotenv()

# Configurando o banco de dados SQLite
DATABASE_URL = os.getenv('DATABASE_URL') # O banco será criado no diretório local com esse nome

# Criação do engine e da sessão do SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


# # Consulta SQL direta
# query = text("SELECT * FROM Album LIMIT 10;")  # Exemplo de consulta

# # Conectando ao banco e executando a consulta
# with engine.connect() as connection:
#     result = connection.execute((query))
    
#     # Exibindo os resultados
#     for row in result:
#         print(row)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Base para os modelos de banco de dados
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
