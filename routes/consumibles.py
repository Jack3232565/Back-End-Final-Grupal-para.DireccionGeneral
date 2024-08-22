from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from portadortoken import Portador  
from typing import List
import crud.consumibles, config.db, schemas.consumibles, models.consumibles

consumible = APIRouter()

# Crear todas las tablas en la base de datos
models.consumibles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@consumible.get("/consumibles/", response_model=List[schemas.consumibles.Consumible], tags=["Consumibles"], dependencies=[Depends(Portador())])
def read_consumibles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_consumibles = crud.consumibles.get_consumibles(db=db, skip=skip, limit=limit)
    return db_consumibles

@consumible.get("/consumible/{ID}", response_model=schemas.consumibles.Consumible, tags=["Consumibles"],dependencies=[Depends(Portador())])
def read_consumible(ID: int, db: Session = Depends(get_db)):
    db_consumible = crud.consumibles.get_consumible(db=db, ID=ID)
    if db_consumible is None:
        raise HTTPException(status_code=404, detail="Consumible no encontrado")
    return db_consumible

@consumible.post("/consumibles/", response_model=schemas.consumibles.Consumible, tags=["Consumibles"])
def create_consumible(consumible: schemas.consumibles.ConsumibleCreate, db: Session = Depends(get_db)):
    db_consumible = crud.consumibles.get_consumibles_by_nombre(db, Nombre=consumible.Nombre)
    if db_consumible:
        raise HTTPException(status_code=400, detail="Consumible existente, intenta nuevamente")
    return crud.consumibles.create_consumible(db=db, consumible=consumible)

@consumible.put("/consumible/{ID}", response_model=schemas.consumibles.Consumible, tags=["Consumibles"],dependencies=[Depends(Portador())])
def update_consumible(ID: int, consumible: schemas.consumibles.ConsumibleUpdate, db: Session = Depends(get_db)):
    db_consumible = crud.consumibles.update_consumible(db=db, ID=ID, consumible=consumible)
    if db_consumible is None:
        raise HTTPException(status_code=404, detail="Consumible no existente, no se actualizó")
    return db_consumible

@consumible.delete("/consumible/{ID}", response_model=schemas.consumibles.Consumible, tags=["Consumibles"],dependencies=[Depends(Portador())])
def delete_consumible(ID: int, db: Session = Depends(get_db)):
    db_consumible = crud.consumibles.delete_consumible(db=db, ID=ID)
    if db_consumible is None:
        raise HTTPException(status_code=404, detail="Consumible no existe, no se pudo eliminar")
    return db_consumible
