from fastapi import APIRouter,Depends,HTTPException,status,Response
from ..database import get_db
from ..auth import verify_password,create_acess_token
from app.crud.userCrud import getByEmail
from ..schemas.userSchema import UserLogin
from sqlalchemy.orm import Session


router = APIRouter()





# Endpoint para autenticar e gerar o token JWT
@router.post("/user/token")
def login_for_access_token(login: UserLogin, db: Session = Depends(get_db)):
    user = getByEmail(db, login.Email)
    if not user :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_acess_token(data={"sub": login.Email})

  # Armazena o token no cookie (comumente chamado de "access_token")
    Response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True, samesite="Lax")

    return {"access_token": access_token, "token_type": "bearer"}