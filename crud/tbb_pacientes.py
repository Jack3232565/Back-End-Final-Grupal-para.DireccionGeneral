from sqlalchemy.orm import Session
import models.tbb_pacientes
import schemas.tbb_pacientes

def create_paciente(db: Session, paciente: schemas.tbb_pacientes.TbbPacientesCreate):
    db_paciente = models.tbb_pacientes.TbbPacientes(
        Persona_ID=paciente.Persona_ID,
        NSS=paciente.NSS,
        Tipo_Seguro=paciente.Tipo_Seguro,
        Fecha_Ultima_Cita=paciente.Fecha_Ultima_Cita,
        Fecha_Registro=paciente.Fecha_Registro,
        Estatus_Medico=paciente.Estatus_Medico,
        Estatus_Vida=paciente.Estatus_Vida,
        Estatus=paciente.Estatus
    )
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def get_paciente(db: Session, persona_id: int):
    return db.query(models.tbb_pacientes.TbbPacientes).filter(models.tbb_pacientes.TbbPacientes.Persona_ID == persona_id).first()

def get_pacientes(db: Session):
    return db.query(models.tbb_pacientes.TbbPacientes).all()

def update_paciente(db: Session, persona_id: int, paciente: schemas.tbb_pacientes.TbbPacientesUpdate):
    db_paciente = db.query(models.tbb_pacientes.TbbPacientes).filter(models.tbb_pacientes.TbbPacientes.Persona_ID == persona_id).first()
    if db_paciente is None:
        return None
    for key, value in paciente.dict().items():
        if value is not None:
            setattr(db_paciente, key, value)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def delete_paciente(db: Session, persona_id: int):
    db_paciente = db.query(models.tbb_pacientes.TbbPacientes).filter(models.tbb_pacientes.TbbPacientes.Persona_ID == persona_id).first()
    if db_paciente is None:
        return None
    db.delete(db_paciente)
    db.commit()
    return db_paciente