from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from portadortoken import Portador
import crud.espacios, config.db, schemas.espacios, models.espacios

espacio = APIRouter()

models.espacios.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@espacio.get("/espacios/", response_model=List[schemas.espacios.Espacio], tags=["Espacios"],dependencies=[Depends(Portador())])
def read_espacios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_espacios = crud.espacios.get_espacios(db=db, skip=skip, limit=limit)
    return db_espacios

@espacio.get("/espacios/{id}", response_model=schemas.espacios.Espacio, tags=["Espacios"],dependencies=[Depends(Portador())])
def read_espacio(id: int, db: Session = Depends(get_db)):
    db_espacio = crud.espacios.get_espacio(db=db, id=id)
    if db_espacio is None:
        raise HTTPException(status_code=404, detail="Espacio no encontrado")
    return db_espacio

@espacio.post("/espacios/", response_model=schemas.espacios.Espacio, tags=["Espacios"],dependencies=[Depends(Portador())])
def create_espacio(espacio: schemas.espacios.EspacioCreate, db: Session = Depends(get_db)):
    return crud.espacios.create_espacio(db=db, espacio=espacio)

@espacio.put("/espacios/{id}", response_model=schemas.espacios.Espacio, tags=["Espacios"],dependencies=[Depends(Portador())])
def update_espacio(id: int, espacio: schemas.espacios.EspacioUpdate, db: Session = Depends(get_db)):
    db_espacio = crud.espacios.update_espacio(db=db, id=id, espacio=espacio)
    if db_espacio is None:
        raise HTTPException(status_code=404, detail="Espacio no encontrado")
    return db_espacio

@espacio.delete("/espacios/{id}", response_model=schemas.espacios.Espacio, tags=["Espacios"],dependencies=[Depends(Portador())])
def delete_espacio(id: int, db: Session = Depends(get_db)):
    db_espacio = crud.espacios.delete_espacio(db=db, id=id)
    if db_espacio is None:
        raise HTTPException(status_code=404, detail="Espacio no encontrado")
    return db_espacio
