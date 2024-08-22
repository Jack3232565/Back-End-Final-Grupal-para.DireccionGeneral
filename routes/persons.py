from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.persons, config.db, schemas.persons, models.persons
from typing import List
from portadortoken import Portador
from datetime import datetime
import os
import shutil

key = Fernet.generate_key()
f = Fernet(key)

person = APIRouter()

models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIRECTORY = "./uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@person.get("/persons/", response_model=List[schemas.persons.Person], tags=["Tbb_Personas"])
def read_persons( db: Session = Depends(get_db)):
    db_persons = crud.persons.get_persons(db=db)
    return db_persons

@person.get("/person/{id}", response_model=schemas.persons.Person, tags=["Tbb_Personas"])
def read_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.persons.get_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_person

@person.post("/person/", response_model=schemas.persons.Person, tags=["Tbb_Personas"])
async def create_person(
    Titulo_Cortesia: str = Form(...),
    Nombre: str = Form(...),
    Primer_Apellido: str = Form(...),
    Segundo_Apellido: str = Form(None),
    CURP: str = Form(...),
    Fecha_Nacimiento: str = Form(...),
    Genero: str = Form(...),
    Tipo_Sangre: str = Form(...),
    Fotografia: UploadFile = File(...),
    Estatus: bool = Form(True),
    db: Session = Depends(get_db)
):
    file_location = f"{UPLOAD_DIRECTORY}/{Fotografia.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(Fotografia.file, file_object)

    person_data = schemas.persons.PersonCreate(
        Titulo_Cortesia=Titulo_Cortesia,
        Nombre=Nombre,
        Primer_Apellido=Primer_Apellido,
        Segundo_Apellido=Segundo_Apellido,
        CURP=CURP,
        Fecha_Nacimiento=datetime.strptime(Fecha_Nacimiento, "%Y-%m-%d").date(),
        Fotografia=file_location,
        Genero=Genero,
        Tipo_Sangre=Tipo_Sangre,
        Estatus=Estatus,
        Fecha_Registro=datetime.now(),
        Fecha_Actualizacion=datetime.now()
    )

    db_person = crud.persons.get_person_by_nombre(db, person=Nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.persons.create_person(db=db, person=person_data)

@person.put("/person/{id}", response_model=schemas.persons.Person, tags=["Tbb_Personas"], dependencies=[Depends(Portador())])
async def update_person(
    id: int,
    Titulo_Cortesia: str = Form(...),
    Nombre: str = Form(...),
    Primer_Apellido: str = Form(...),
    Segundo_Apellido: str = Form(None),
    CURP: str = Form(...),
    Fecha_Nacimiento: str = Form(...),
    Genero: str = Form(...),
    Tipo_Sangre: str = Form(...),
    Fotografia: UploadFile = File(None),
    Estatus: bool = Form(True),
    db: Session = Depends(get_db)
):
    file_location = None
    if Fotografia:
        file_location = f"{UPLOAD_DIRECTORY}/{Fotografia.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(Fotografia.file, file_object)

    person_data = schemas.persons.PersonUpdate(
        Titulo_Cortesia=Titulo_Cortesia,
        Nombre=Nombre,
        Primer_Apellido=Primer_Apellido,
        Segundo_Apellido=Segundo_Apellido,
        CURP=CURP,
        Fecha_Nacimiento=datetime.strptime(Fecha_Nacimiento, "%Y-%m-%d").date(),
        Fotografia=file_location if file_location else None,
        Genero=Genero,
        Tipo_Sangre=Tipo_Sangre,
        Estatus=Estatus,
        Fecha_Registro=datetime.now(),
        Fecha_Actualizacion=datetime.now()
    )

    db_person = crud.persons.update_person(db=db, id=id, person=person_data)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizado")
    return db_person

@person.delete("/person/{id}", response_model=schemas.persons.Person, tags=["Tbb_Personas"], dependencies=[Depends(Portador())])
def delete_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.persons.delete_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_person

