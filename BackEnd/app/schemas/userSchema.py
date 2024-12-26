# app/schemas.py
from pydantic import BaseModel
from typing import Optional

# Para criar um novo usuário
class UserBase(BaseModel):

    Nome: str
    Email: str
    Senha: str
    Nivel_Acesso: str


# Para resposta com dados do usuário
class UserCreate(UserBase):
    pass


class User(UserBase):
    
     UserId:int

     class Config:
        orm_mode = True  # Permite que o Pydantic converta objetos do SQLAlchemy
        

class UserUpdate(UserBase):
     Nome: Optional[str] = None
     Email: Optional[str] = None
     Senha: Optional[str] = None
     Nivel_Acesso: Optional[str] = None


class UserLogin(UserBase):

    Nome: Optional[str] = None
    Senha: Optional[str] = None
    Nivel_Acesso: Optional[str] = None