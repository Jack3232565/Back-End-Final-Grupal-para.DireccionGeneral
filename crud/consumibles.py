import models.consumibles
import schemas.consumibles
from sqlalchemy.orm import Session

def get_consumible(db: Session, ID: int):
    return db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.ID == ID).first()

def get_consumibles_by_nombre(db: Session, Nombre: str):

    return db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.Nombre == Nombre).first()

def get_consumibles(db: Session, skip: int = 0, limit: int = 10):

    return db.query(models.consumibles.Consumible).offset(skip).limit(limit).all()

def create_consumible(db: Session, consumible: schemas.consumibles.ConsumibleCreate):

    db_consumible = models.consumibles.Consumible(
        Nombre=consumible.Nombre,
        Descripcion=consumible.Descripcion,
        Cantidad=consumible.Cantidad,
        Tipo=consumible.Tipo,
        Departamento_ID=consumible.Departamento_ID,
        Estatus=consumible.Estatus,
        Fecha_Registro=consumible.Fecha_Registro,
        Fecha_Actualizacion=consumible.Fecha_Actualizacion,
        Observaciones=consumible.Observaciones,
        Espacio_Medico=consumible.Espacio_Medico
    )
    db.add(db_consumible)
    db.commit()
    db.refresh(db_consumible)
    return db_consumible

def update_consumible(db: Session, ID: int, consumible: schemas.consumibles.ConsumibleUpdate):
    db_consumible = db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.ID == ID).first()
    if db_consumible:
        for var, value in vars(consumible).items():
            setattr(db_consumible, var, value) if value is not None else None
        db.commit()
        db.refresh(db_consumible)
    return db_consumible

def delete_consumible(db: Session, ID: int):
    db_consumible = db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.ID == ID).first()
    if db_consumible:
        db.delete(db_consumible)
        db.commit()
    return db_consumible

