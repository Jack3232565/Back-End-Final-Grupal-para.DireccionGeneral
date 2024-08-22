from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
import crud.puestos_departamentos, config.db, schemas.puestos_departamentos, models.puestos_departamentos
from jwt_config import solicita_token
from portadortoken import Portador

puesto_departamento = APIRouter()

models.puestos_departamentos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@puesto_departamento.get("/puestos_departamentos/", response_model=List[schemas.puestos_departamentos.PuestoDepartamento], tags=["Puestos_Departamentos"], dependencies=[Depends(Portador())])
def read_puestos_departamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_puestos_departamentos = crud.puestos_departamentos.get_puestos_departamentos(db=db, skip=skip, limit=limit)
    return db_puestos_departamentos

@puesto_departamento.get("/puesto_departamento/{id}", response_model=schemas.puestos_departamentos.PuestoDepartamento, tags=["Puestos_Departamentos"], dependencies=[Depends(Portador())])
def read_puesto_departamento(id: int, db: Session = Depends(get_db)):
    db_puesto_departamento = crud.puestos_departamentos.get_puesto_departamento(db=db, id=id)
    if db_puesto_departamento is None:
        raise HTTPException(status_code=404, detail="Puesto departamento no encontrado")
    return db_puesto_departamento

@puesto_departamento.post("/puestos_departamentos/", response_model=schemas.puestos_departamentos.PuestoDepartamento, tags=["Puestos_Departamentos"])
def create_puesto_departamento(puesto_departamento: schemas.puestos_departamentos.PuestoDepartamentoCreate, db: Session = Depends(get_db)):
    db_puesto_departamento = crud.puestos_departamentos.get_puesto_departamento_by_nombre(db, nombre=puesto_departamento.Nombre)
    if db_puesto_departamento:
        raise HTTPException(status_code=400, detail="El nombre del puesto departamento ya existe")
    return crud.puestos_departamentos.create_puesto_departamento(db=db, puesto_departamento=puesto_departamento)

@puesto_departamento.put("/puesto_departamento/{id}", response_model=schemas.puestos_departamentos.PuestoDepartamento, tags=["Puestos_Departamentos"], dependencies=[Depends(Portador())])
def update_puesto_departamento(id: int, puesto_departamento: schemas.puestos_departamentos.PuestoDepartamentoUpdate, db: Session = Depends(get_db)):
    db_puesto_departamento = crud.puestos_departamentos.update_puesto_departamento(db=db, id=id, puesto_departamento=puesto_departamento)
    if db_puesto_departamento is None:
        raise HTTPException(status_code=404, detail="Puesto departamento no encontrado, no se pudo actualizar")
    return db_puesto_departamento

@puesto_departamento.delete("/puesto_departamento/{id}", response_model=schemas.puestos_departamentos.PuestoDepartamento, tags=["Puestos_Departamentos"], dependencies=[Depends(Portador())])
def delete_puesto_departamento(id: int, db: Session = Depends(get_db)):
    db_puesto_departamento = crud.puestos_departamentos.delete_puesto_departamento(db=db, id=id)
    if db_puesto_departamento is None:
        raise HTTPException(status_code=404, detail="Puesto departamento no encontrado, no se pudo eliminar")
    return db_puesto_departamento
