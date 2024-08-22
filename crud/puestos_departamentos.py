import models.puestos_departamentos
import schemas.puestos_departamentos
from sqlalchemy.orm import Session

def get_puesto_departamento(db: Session, id: int):
    return db.query(models.puestos_departamentos.PuestoDepartamento).filter(models.puestos_departamentos.PuestoDepartamento.PuestoID == id).first()

def get_puesto_departamento_by_nombre(db: Session, nombre: str):
    return db.query(models.puestos_departamentos.PuestoDepartamento).filter(models.puestos_departamentos.PuestoDepartamento.Nombre == nombre).first()

def get_puestos_departamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.puestos_departamentos.PuestoDepartamento).offset(skip).limit(limit).all()

def create_puesto_departamento(db: Session, puesto_departamento: schemas.puestos_departamentos.PuestoDepartamentoCreate):
    db_puesto_departamento = models.puestos_departamentos.PuestoDepartamento(
        Nombre=puesto_departamento.Nombre,
        Descripcion=puesto_departamento.Descripcion,
        Salario=puesto_departamento.Salario,
        Turno=puesto_departamento.Turno,
        Creado=puesto_departamento.Creado,
        Modificado=puesto_departamento.Modificado,
        DepartamentoID=puesto_departamento.DepartamentoID
    )
    db.add(db_puesto_departamento)
    db.commit()
    db.refresh(db_puesto_departamento)
    return db_puesto_departamento

def update_puesto_departamento(db: Session, id: int, puesto_departamento: schemas.puestos_departamentos.PuestoDepartamentoUpdate):
    db_puesto_departamento = db.query(models.puestos_departamentos.PuestoDepartamento).filter(models.puestos_departamentos.PuestoDepartamento.PuestoID == id).first()
    if db_puesto_departamento:
        for var, value in vars(puesto_departamento).items():
            if value is not None:
                setattr(db_puesto_departamento, var, value)
        db.commit()
        db.refresh(db_puesto_departamento)
    return db_puesto_departamento

def delete_puesto_departamento(db: Session, id: int):
    db_puesto_departamento = db.query(models.puestos_departamentos.PuestoDepartamento).filter(models.puestos_departamentos.PuestoDepartamento.PuestoID == id).first()
    if db_puesto_departamento:
        db.delete(db_puesto_departamento)
        db.commit()
    return db_puesto_departamento
