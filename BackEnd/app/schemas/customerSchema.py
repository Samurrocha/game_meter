

from pydantic import BaseModel,EmailStr
from typing import Optional

# Modelo Base para Customer
class CustomerBase(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Company: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    Country: Optional[str] = None
    PostalCode: Optional[str] = None
    Phone: Optional[str] = None
    Fax: Optional[str] = None
    Email: Optional[str] = None
    SupportRepId: Optional[int] = None

# Modelo para criação de um novo Customer
class CustomerCreate(CustomerBase):
   
   pass

# Modelo de resposta para Customer (com dados do banco)
class Customer(CustomerBase):
    CustomerId: int

    class Config:
        orm_mode = True  # Permite que o Pydantic converta objetos do SQLAlchemy

