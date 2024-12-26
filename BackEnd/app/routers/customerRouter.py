from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..crud import customerCrud
from ..models import userModel
from ..schemas.customerSchema import Customer,CustomerCreate
from ..auth import get_current_user
from ..database import get_db
from typing import Union

router = APIRouter()



#Rota para obter todos customers
@router.get("/customer", response_model= list[Customer])
def read_customers(db: Session = Depends(get_db), user_atual: userModel.User = Depends(get_current_user)):
    
    # Verifica se o usuário tem o role 'admin'
    if user_atual.Nivel_Acesso != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to view all customers.",
        )


    return customerCrud.get_Customers(db)


# Rota para obter um customer por ID
@router.get("/customer/{customer_id}", response_model=Customer)
def get_By_Id(customer_id: int, db: Session = Depends(get_db)):
    customer = customerCrud.getById(db, customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail="customer not found")
    return customer


@router.post("/createcustomer", response_model= Union[Customer, list[Customer]])
def create_customer(customer: Union[CustomerCreate, list[CustomerCreate]], db:Session = Depends(get_db)):
    return customerCrud.create_Customer(db, customer)


