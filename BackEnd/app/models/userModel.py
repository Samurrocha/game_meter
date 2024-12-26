# app/models.py
from sqlalchemy import Column, Integer, String
from ..database import Base

class User(Base):
    __tablename__ = 'User'  # Nome da tabela no banco de dados

    UserId = Column(Integer, primary_key=True, index=True, autoincrement= True)
    Nome = Column(String, index=True)
    Email = Column(String, index=True)
    Senha = Column(String, index=True)
    Nivel_Acesso = Column(String, index=True)

