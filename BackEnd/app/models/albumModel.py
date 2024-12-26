# app/models.py
from sqlalchemy import Column, Integer, String
from ..database import Base

class Album(Base):
    __tablename__ = 'Album'  # Nome da tabela no banco de dados

    AlbumId = Column(Integer, primary_key=True, index=True)
    Title = Column(String, index=True)
    ArtistId = Column(Integer, index=True)
