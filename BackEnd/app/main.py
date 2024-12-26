# app/main.py
from fastapi import FastAPI
from .models import albumModel, customerModel,userModel
from . import database
from .routers import albumRouter,customerRouter,userRouter, authRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

# OAuth2PasswordBearer é necessário para indicar o ponto de onde o token será passado (por exemplo, no header)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Criando as tabelas no banco de dados
database.Base.metadata.create_all(bind=database.engine)

userModel.Base.metadata.create_all(bind=database.engine)
# customerModel.Base.metadata.create_all(bind=database.engine)

app.include_router(albumRouter.router)
app.include_router(customerRouter.router)
app.include_router(userRouter.router)
app.include_router(authRouter.router)