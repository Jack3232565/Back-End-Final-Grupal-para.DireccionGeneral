from sqlalchemy.orm import Session
from models.tbc_departamentos import Departamento
from schemas.tbc_departamentos import DepartamentoCreate, DepartamentoUpdate

def get_departamento(db: Session, departamento_id: int):
    return db.query(Departamento).filter(Departamento.ID == departamento_id).first()

def get_departamentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Departamento).offset(skip).limit(limit).all()

def create_departamento(db: Session, departamento: DepartamentoCreate):
    db_departamento = Departamento(
        Nombre=departamento.Nombre,
        AreaMedica_ID=departamento.AreaMedica_ID,
        Departamento_Superior_ID=departamento.Departamento_Superior_ID,
        Responsable_ID=departamento.Responsable_ID,
        Estatus=departamento.Estatus,
    )
    db.add(db_departamento)
    db.commit()
    db.refresh(db_departamento)
    return db_departamento

def update_departamento(db: Session, departamento_id: int, departamento: DepartamentoUpdate):
    db_departamento = db.query(Departamento).filter(Departamento.ID == departamento_id).first()
    if db_departamento is None:
        return None
    
    for var, value in vars(departamento).items():
        setattr(db_departamento, var, value) if value else None
    
    db.commit()
    db.refresh(db_departamento)
    return db_departamento

def delete_departamento(db: Session, departamento_id: int):
    db_departamento = db.query(Departamento).filter(Departamento.ID == departamento_id).first()
    if db_departamento is None:
        return None
    db.delete(db_departamento)
    db.commit()
    return db_departamento