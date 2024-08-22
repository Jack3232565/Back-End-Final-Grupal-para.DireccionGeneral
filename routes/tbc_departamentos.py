from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.tbc_departamentos as crud
import schemas.tbc_departamentos as schemas
import config.db as db_config


departamentos = APIRouter(tags=["Tbc_Departamentos"])

# Create tables if not already created
import models.tbc_departamentos as models
models.Base.metadata.create_all(bind=db_config.engine)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@departamentos.post("/departamentos/", response_model=schemas.Departamento)
def create_departamento(departamento: schemas.DepartamentoCreate, db: Session = Depends(get_db)):
    db_departamento = crud.create_departamento(db=db, departamento=departamento)
    return db_departamento

@departamentos.get("/departamentos/", response_model=List[schemas.Departamento])
def read_departamentos( db: Session = Depends(get_db)):
    departamentos = crud.get_departamentos(db=db)
    return departamentos

@departamentos.get("/departamentos/{departamento_id}", response_model=schemas.Departamento)
def read_departamento(departamento_id: int, db: Session = Depends(get_db)):
    db_departamento = crud.get_departamento(db=db, departamento_id=departamento_id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return db_departamento

@departamentos.put("/departamentos/{departamento_id}", response_model=schemas.Departamento)
def update_departamento(departamento_id: int, departamento: schemas.DepartamentoUpdate, db: Session = Depends(get_db)):
    db_departamento = crud.update_departamento(db=db, departamento_id=departamento_id, departamento=departamento)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return db_departamento

@departamentos.delete("/departamentos/{departamento_id}", response_model=schemas.Departamento)
def delete_departamento(departamento_id: int, db: Session = Depends(get_db)):
    db_departamento = crud.delete_departamento(db=db, departamento_id=departamento_id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return db_departamento