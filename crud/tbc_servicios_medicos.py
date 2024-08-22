from sqlalchemy.orm import Session
from models.tbc_servicios_medicos import ServicioMedico  # Importa el modelo correcto
from schemas.tbc_servicios_medicos import ServicioMedicoCreate, ServicioMedicoUpdate

def create_servicio(db: Session, servicio: ServicioMedicoCreate):
    db_servicio = ServicioMedico(**servicio.dict())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def get_servicios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ServicioMedico).offset(skip).limit(limit).all()

def get_servicio(db: Session, servicio_id: int):
    return db.query(ServicioMedico).filter(ServicioMedico.ID == servicio_id).first()

def update_servicio(db: Session, servicio_id: int, servicio: ServicioMedicoUpdate):
    db_servicio = db.query(ServicioMedico).filter(ServicioMedico.ID == servicio_id).first()
    if db_servicio:
        for key, value in servicio.dict(exclude_unset=True).items():
            setattr(db_servicio, key, value)
        db.commit()
        db.refresh(db_servicio)
        return db_servicio
    return None

def delete_servicio(db: Session, servicio_id: int):
    db_servicio = db.query(ServicioMedico).filter(ServicioMedico.ID == servicio_id).first()
    if db_servicio:
        db.delete(db_servicio)
        db.commit()
        return db_servicio
    return None