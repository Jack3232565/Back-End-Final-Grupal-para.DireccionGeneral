from sqlalchemy.orm import Session
import models.espacios, schemas.espacios

def get_espacio(db: Session, id: int):
    return db.query(models.espacios.Espacio).filter(models.espacios.Espacio.ID == id).first()

def get_espacios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.espacios.Espacio).offset(skip).limit(limit).all()

def create_espacio(db: Session, espacio: schemas.espacios.EspacioCreate):
    db_espacio = models.espacios.Espacio(**espacio.dict())
    db.add(db_espacio)
    db.commit()
    db.refresh(db_espacio)
    return db_espacio

def update_espacio(db: Session, id: int, espacio: schemas.espacios.EspacioUpdate):
    db_espacio = db.query(models.espacios.Espacio).filter(models.espacios.Espacio.ID == id).first()
    if db_espacio:
        for var, value in vars(espacio).items():
            setattr(db_espacio, var, value) if value else None
        db.commit()
        db.refresh(db_espacio)
    return db_espacio

def delete_espacio(db: Session, id: int):
    db_espacio = db.query(models.espacios.Espacio).filter(models.espacios.Espacio.ID == id).first()
    if db_espacio:
        db.delete(db_espacio)
        db.commit()
    return db_espacio
