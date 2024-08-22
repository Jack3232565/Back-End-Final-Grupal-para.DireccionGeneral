import models.areas_medicas
import schemas.areas_medicas
from sqlalchemy.orm import Session

def get_area_medica(db: Session, id: int):
    return db.query(models.areas_medicas.AreaMedica).filter(models.areas_medicas.AreaMedica.ID == id).first()

def get_area_medica_by_nombre(db: Session, nombre: str):
    return db.query(models.areas_medicas.AreaMedica).filter(models.areas_medicas.AreaMedica.Nombre == nombre).first()

def get_areas_medicas(db: Session):
    return db.query(models.areas_medicas.AreaMedica).all()

def create_area_medica(db: Session, area: schemas.areas_medicas.AreaMedicaCreate):
    db_area = models.areas_medicas.AreaMedica(
        Nombre=area.Nombre,
        Descripcion=area.Descripcion,
        Estatus=area.Estatus,
        Fecha_Registro=area.Fecha_Registro,
        Fecha_Actualizacion=area.Fecha_Actualizacion
    )
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area

def update_area_medica(db: Session, id: int, area: schemas.areas_medicas.AreaMedicaUpdate):
    db_area = db.query(models.areas_medicas.AreaMedica).filter(models.areas_medicas.AreaMedica.ID == id).first()
    if db_area:
        for var, value in vars(area).items():
            if value is not None:
                setattr(db_area, var, value)
        db.commit()
        db.refresh(db_area)
    return db_area

def delete_area_medica(db: Session, id: int):
    db_area = db.query(models.areas_medicas.AreaMedica).filter(models.areas_medicas.AreaMedica.ID == id).first()
    if db_area:
        db.delete(db_area)
        db.commit()
    return db_area
