# app/schemas.py
from pydantic import BaseModel
from typing import Optional

# Para criar um novo usuário
class AlbumBase(BaseModel):
    Title: Optional[str] = None
    ArtistId: Optional[int] = None

# Para resposta com dados do usuário
class AlbumCreate(AlbumBase):
    pass


class Album(AlbumBase):
     AlbumId : int

     class Config:
        orm_mode = True  # Permite que o Pydantic converta objetos do SQLAlchemy
        
