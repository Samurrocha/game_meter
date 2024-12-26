from jose import jwt,JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status,Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.crud import userCrud
from .database import get_db
from datetime import datetime, timedelta,timezone
from typing import Optional
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env (caso necessário)
load_dotenv()

# Configurando o banco de dados SQLite
SECRET_KEY = os.getenv('SECRET_KEY')

ALGORITHM = os.getenv('ALGORITHM')

EXPIRE_TIME = int(os.getenv('EXPIRE_TIME'))
expiration_time = datetime.now(timezone.utc) + timedelta(minutes='EXPIRE_TIME')


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



utc_now = datetime.now(timezone.utc)

def verify_password(plain_pwd: str, hashed_pwd: str)->bool:
    return pwd_context.verify(plain_pwd, hashed_pwd)

def get_hashed_pwd(pwd:str)->str:
    return pwd_context.hash(pwd)


#criar Token
def create_acess_token(data: dict):
    to_encode = data.copy()

    to_encode.update({"exp": expiration_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




# Função para obter o token a partir do cookie
def get_token_from_cookie() -> Optional[str]:
    token = Request.cookies.get("access_token")  # Nome do cookie
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

#verificar Token
def verify_token(token: str = Depends(get_token_from_cookie)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email:str = payload.get("sub")
        
        return email
    except JWTError:
        return None


def get_current_user(db: Session = Depends(get_db), data:str = Depends(verify_token)):
    user = userCrud.getByEmail(db,data)
    print(data)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user