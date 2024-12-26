# app/crud.py
from sqlalchemy.orm import Session
from ..models.userModel import User
from ..schemas.userSchema import UserCreate, UserUpdate
from app import auth
from typing import Union



# Obter todos os usuários
def get_users(db: Session):

 return db.query(User).all()

# Obter um usuário pelo ID
def getById(db: Session, User_id: int):
    return db.query(User).filter(User.UserId == User_id).first()


# Obter um usuário pelo ID
def getByEmail(db: Session, user_email: str):
    return db.query(User).filter(User.Email == user_email).first()


#criar um novo User
def create_User(db:Session, user: Union[UserCreate, list[UserCreate]]):
   
  users = []

  if isinstance(user,list):
    for object in user:
      hashed_pwd = auth.get_hashed_pwd(object.Senha)
      new_User = User(Nome = object.Nome, Email = object.Email, Nivel_Acesso = object.Nivel_Acesso, Senha = hashed_pwd)
      users.append(new_User)
  
    db.add_all(users)
    db.commit()

    for object in users:
      db.refresh(object)

    return users
    
  else:

    hashed_pwd = auth.get_hashed_pwd(user.Senha)
    new_User = User(Nome = user.Nome, Email = user.Email, Nivel_Acesso = user.Nivel_Acesso, Senha = hashed_pwd)
    db.add(new_User)
    db.commit()
    db.refresh(new_User)

    return new_User 


def update_User(db:Session, user_id : int, UserUpdated: UserUpdate):
   user = db.query(User).filter(User.UserId == user_id).first()

   if user:
    if UserUpdated.Nome:
      user.Nome = UserUpdated.Nome

    if UserUpdated.Email:
      user.Email = UserUpdated.Email  

    if UserUpdated.Senha :
      user.Senha = UserUpdated.Senha
    

    db.commit()
    db.refresh(user)

    return user
   

def delete_User(db:Session,user_id:int):
  user = db.query(User).filter(User.UserId == user_id).first()

  if user:
    db.delete(user)

    db.commit()


  return user    
   
   


