from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..crud import userCrud
from ..schemas.userSchema import User,UserCreate,UserUpdate
from ..database import get_db
from ..auth import get_current_user
from ..models import userModel
from typing import Union

router = APIRouter()


#criar um unico user
@router.post("/user", response_model=Union[User,list[User]])
def create_user(user: Union[UserCreate,list[UserCreate]], db: Session = Depends(get_db), user_atual: userModel.User = Depends(get_current_user)):

    if user_atual.Nivel_Acesso != "admin":
        raise HTTPException(
             status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to create a user",
        )

    return userCrud.create_User(db, user)



# # Rota para listar todos os usuários
@router.get("/user", response_model= list[User])
def get_User(db:Session = Depends(get_db)):
    return userCrud.get_users(db)



# Rota para obter um usuário por ID
@router.get("/user/{User_id}", response_model=User)
def get_UserBy_Id(User_id: int, db: Session = Depends(get_db)):
    User = userCrud.getById(db, User_id)
    if not User:
        raise HTTPException(status_code=404, detail="User not found")
    return User


# Rota para obter um usuário por ID
@router.get("/user/{user_email}", response_model=User)
def get_by_email(user_email: str, db: Session = Depends(get_db)):
    User = userCrud.getByEmail(db, user_email)
    if not User:
        raise HTTPException(status_code=404, detail="User not found")
    return User


# Rota para atualizar um usuário
@router.put("/user/{user_id}", response_model=User)
def update_User(user_id : int, user : UserUpdate, db: Session = Depends(get_db)):
   return userCrud.update_User(db, user_id, user)


#Rota para deletar User

@router.delete("/user/{user_id}", response_model=User)
def delete_User(user_id:int, db: Session = Depends(get_db)):
    return userCrud.delete_User(db, user_id)