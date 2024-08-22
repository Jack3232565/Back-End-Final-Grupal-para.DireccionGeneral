from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import crud.tbb_pacientes, config.db, schemas.tbb_pacientes, models.tbb_pacientes
from typing import List

tbb_pacientes = APIRouter(tags=["Tbb_Pacientes"])

models.tbb_pacientes.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@tbb_pacientes.post("/tbb_pacientes/", response_model=schemas.tbb_pacientes.TbbPacientes)
def create_paciente(paciente: schemas.tbb_pacientes.TbbPacientesCreate, db: Session = Depends(get_db)):
    try:
        return crud.tbb_pacientes.create_paciente(db, paciente)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="El paciente ya existe.")

@tbb_pacientes.get("/tbb_pacientes/{persona_id}", response_model=schemas.tbb_pacientes.TbbPacientes)
def read_paciente(persona_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.tbb_pacientes.get_paciente(db, persona_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_paciente

@tbb_pacientes.get("/tbb_pacientes/", response_model=List[schemas.tbb_pacientes.TbbPacientes])
def read_pacientes( db: Session = Depends(get_db)):
    return crud.tbb_pacientes.get_pacientes(db)

@tbb_pacientes.put("/tbb_pacientes/{persona_id}", response_model=schemas.tbb_pacientes.TbbPacientes)
def update_paciente(persona_id: int, paciente: schemas.tbb_pacientes.TbbPacientesUpdate, db: Session = Depends(get_db)):
    db_paciente = crud.tbb_pacientes.update_paciente(db, persona_id, paciente)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_paciente

@tbb_pacientes.delete("/tbb_pacientes/{persona_id}", response_model=schemas.tbb_pacientes.TbbPacientes)
def delete_paciente(persona_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.tbb_pacientes.delete_paciente(db, persona_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_paciente