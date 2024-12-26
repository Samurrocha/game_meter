from sqlalchemy import Column, Integer,String, ForeignKey
from ..database import Base

class Customer(Base):
    __tablename__ = 'Customer'

    CustomerId = Column(Integer, primary_key=True, autoincrement= True)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    Company = Column(String(100))
    Address = Column(String(200))
    City = Column(String(100))
    State = Column(String(50))
    Country = Column(String(50))
    PostalCode = Column(String(20))
    Phone = Column(String(50))
    Fax = Column(String(50))
    Email = Column(String(100), unique=True, nullable=False)
    SupportRepId = Column(Integer)