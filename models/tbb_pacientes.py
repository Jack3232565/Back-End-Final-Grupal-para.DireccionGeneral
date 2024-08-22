from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, BINARY
from sqlalchemy.orm import relationship
from config.db import Base
import enum
from datetime import datetime

class EstatusVidaEnum(enum.Enum):
    Vivo = 'Vivo'
    Finado = 'Finado'
    Coma = 'Coma'
    Vegetativo = 'Vegetativo'

class TbbPacientes(Base):
    __tablename__ = 'tbb_pacientes'
    
    Persona_ID = Column(Integer, ForeignKey('tbb_personas.id'), primary_key=True, autoincrement=False)
    NSS = Column(String(15), unique=True, nullable=True)
    Tipo_Seguro = Column(String(50), nullable=False)
    Fecha_Ultima_Cita = Column(DateTime, nullable=True)
    Estatus_Medico = Column(String(100), default='Normal')
    Estatus_Vida = Column(Enum(EstatusVidaEnum), nullable=False, default=EstatusVidaEnum.Vivo)
    Estatus = Column(BINARY(1), default=b'\x01')
    Fecha_Registro = Column(DateTime, nullable=False, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, nullable=True)

    persona = relationship("Person", back_populates="paciente")
    
