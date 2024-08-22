from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from config.db import Base
from sqlalchemy.orm import relationship
import enum

class Estatus(str, enum.Enum):
    Registrada = "Registrada"
    Programada = "Programada"
    Cancelada = "Cancelada"
    Reprogramada = "Reprogramada"
    En_Proceso = "En Proceso"
    Realizada = "Realizada"
    Aprobado = "Aprobado"

class Tipo(str, enum.Enum):
    Servicio_Interno = "Servicio Interno"
    Traslados = "Traslados"
    Subrogado = "Subrogado"
    Administrativo = "Administrativo"

class Aprobaciones(Base):
    __tablename__ = "tbb_aprobaciones"
    id = Column(Integer, primary_key=True, index=True)
    Personal_Medico_ID = Column(Integer, ForeignKey("tbb_personal_medico.Persona_ID"), nullable=False)
    # Personal_Medico_ID = Column(Integer)
    Solicitud_id = Column(Integer, ForeignKey("tbd_solicitudes.ID"), nullable=False)
    # Solicitud_id = Column(Integer)
    Comentario = Column(String(500))
    Estatus = Column(Enum(Estatus))
    Tipo = Column(Enum(Tipo))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime, nullable=True, default=None)

    personal_medico = relationship("PersonalMedico", back_populates="aprobaciones")
    solicitudes = relationship("Solicitud", back_populates="aprobaciones")