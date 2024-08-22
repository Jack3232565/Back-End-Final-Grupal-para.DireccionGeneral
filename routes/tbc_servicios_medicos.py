# routes/tbc_servicios_medicos.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.tbc_servicios_medicos as crud
import models.tbc_servicios_medicos
import config.db as db_config
from schemas.tbc_servicios_medicos import ServicioMedico, ServicioMedicoCreate, ServicioMedicoUpdate


servicios_medicos = APIRouter()

models.tbc_servicios_medicos.Base.metadata.create_all(bind=db_config.engine)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@servicios_medicos.get("/servicios/", response_model=List[ServicioMedico], tags=["Tbc_Servicios_Medicos"])
def read_servicios(db: Session = Depends(get_db)):
    db_servicios = crud.get_servicios(db=db)
    if db_servicios is None:
        raise HTTPException(status_code=404, detail="Servicios no encontrados")
    return db_servicios

@servicios_medicos.get("/servicios/{servicio_id}", response_model=ServicioMedico, tags=["Tbc_Servicios_Medicos"])
def read_servicio(servicio_id: int, db: Session = Depends(get_db)):
    db_servicio = crud.get_servicio(db=db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@servicios_medicos.post("/servicios/", response_model=ServicioMedico, tags=["Tbc_Servicios_Medicos"])
def create_servicio(servicio: ServicioMedicoCreate, db: Session = Depends(get_db)):
    db_servicio = crud.create_servicio(db=db, servicio=servicio)
    return db_servicio

@servicios_medicos.put("/servicios/{servicio_id}", response_model=ServicioMedico, tags=["Tbc_Servicios_Medicos"])
def update_servicio(servicio_id: int, servicio: ServicioMedicoUpdate, db: Session = Depends(get_db)):
    db_servicio = crud.update_servicio(db=db, servicio_id=servicio_id, servicio=servicio)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@servicios_medicos.delete("/servicios/{servicio_id}", response_model=ServicioMedico, tags=["Tbc_Servicios_Medicos"])
def delete_servicio(servicio_id: int, db: Session = Depends(get_db)):
    db_servicio = crud.delete_servicio(db=db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio