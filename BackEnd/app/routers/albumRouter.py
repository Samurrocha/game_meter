from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import albumCrud
from ..schemas.albumSchemas import Album,AlbumCreate
from ..database import get_db

router = APIRouter()



@router.post("/album", response_model=Album)
def create_user(album: AlbumCreate, db: Session = Depends(get_db)):
    return albumCrud.create_Album(db, album)


# # Rota para listar todos os usuários
@router.get("/album", response_model= list[Album])
def get_album(db:Session = Depends(get_db)):
    return albumCrud.get_Albuns(db)



# Rota para obter um usuário por ID
@router.get("/album/{album_id}", response_model=Album)
def get_AlbumBy_Id(album_id: int, db: Session = Depends(get_db)):
    album = albumCrud.getById(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album



# Rota para atualizar um usuário
@router.put("/album/{album_id}", response_model=Album)
def update_Album(album_id : int, album : AlbumCreate, db: Session = Depends(get_db)):
   return albumCrud.update_Album(db, album_id, album)



#Rota para deletar Album

@router.delete("/album/{album_id}", response_model=Album)
def delete_Album(album_id:int, db: Session = Depends(get_db)):
    return albumCrud.delete_Album(db, album_id)

