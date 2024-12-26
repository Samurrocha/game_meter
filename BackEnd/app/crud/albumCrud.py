# app/crud.py
from sqlalchemy.orm import Session
from app.models.albumModel import Album
from app.schemas.albumSchemas import AlbumCreate



# Obter todos os usuários
def get_Albuns(db: Session):

 return db.query(Album).all()

# Obter um usuário pelo ID
def getById(db: Session, album_id: int):
    return db.query(Album).filter(Album.AlbumId == album_id).first()

#criar um novo album
def create_Album(db:Session, album:AlbumCreate):
   new_album = Album(Title = album.Title, ArtistId = album.ArtistId)
   db.add(new_album)
   db.commit()
   db.refresh(new_album)

   return new_album 


def update_Album(db:Session, album_id : int, albumUpdated: AlbumCreate):
   album = db.query(Album).filter(Album.AlbumId == album_id).first()

   if album:
    if albumUpdated.Title:
      album.Title = albumUpdated.Title

    if albumUpdated.ArtistId:
      album.ArtistId = albumUpdated.ArtistId  
    

    db.commit()
    db.refresh(album)

    return album
   

def delete_Album(db:Session,album_id:int):
  album = db.query(Album).filter(Album.AlbumId == album_id).first()

  if album:
    db.delete(album)

    db.commit()


  return album    
   
   


