# app/crud.py
from sqlalchemy.orm import Session
from app.models.customerModel import Customer
from app.schemas.customerSchema import CustomerCreate
from typing import Union



# Obter todos os usuários
def get_Customers(db: Session):

 return db.query(Customer).all()

# Obter um usuário pelo ID
def getById(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.CustomerId == customer_id).first()

#criar um novo Customer
def create_Customer(db:Session, customer: Union[CustomerCreate, list[CustomerCreate]]):
   

  if isinstance(customer, list):

    customers=[]

    for obj in customer:
      new_customer = Customer(
        FirstName = obj.FirstName,
        LastName = obj.LastName,
        Company = obj.Company,
        Address = obj.Address,
        City = obj.City,
        State = obj.State,
        Country = obj.Country,
        PostalCode = obj.PostalCode,
        Phone = obj.Phone,
        Fax = obj.Fax,
        Email = obj.Email,
        SupportRepId = obj.SupportRepId
        )

      customers.append(new_customer)

    db.add_all(customers)
    db.commit()

    for obj in customers:
      db.refresh(obj) 
  
    return customers 
  
  new_customer = Customer(
  FirstName = customer.FirstName,
  LastName = customer.LastName,
  Company = customer.Company,
  Address = customer.Address,
  City = customer.City,
  State = customer.State,
  Country = customer.Country,
  PostalCode = customer.PostalCode,
  Phone = customer.Phone,
  Fax = customer.Fax,
  Email = customer.Email,
  SupportRepId = customer.SupportRepId
)

  db.add(new_customer)
  db.commit()
  db.refresh(new_customer)

  return new_customer


def update_Customer(db:Session, Customer_id : int, CustomerUpdated: CustomerCreate):
   Customer = db.query(Customer).filter(Customer.CustomerId == Customer_id).first()

   if Customer:
    if CustomerUpdated.Title:
      Customer.Title = CustomerUpdated.Title

    if CustomerUpdated.ArtistId:
      Customer.ArtistId = CustomerUpdated.ArtistId  
    

    db.commit()
    db.refresh(Customer)

    return Customer
   

def delete_Customer(db:Session,Customer_id:int):
  Customer = db.query(Customer).filter(Customer.CustomerId == Customer_id).first()

  if Customer:
    db.delete(Customer)

    db.commit()


  return Customer    
   
   


