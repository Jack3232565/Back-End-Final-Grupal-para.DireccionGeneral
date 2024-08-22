from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyEstatus(str, enum.Enum):
    Registrada = "Registrada"
    Programada = "Programada"
    Cancelada = "Cancelada"
    Reprogramada = "Reprogramada"
    En_Proceso = "En Proceso"
    Realizada = "Realizada"
    Aprobado = "Aprobado"

class MyPrioridad(str, enum.Enum):
    Urgente = "Urgente"
    Alta = "Alta"
    Moderada = "Moderada"
    Emergente = "Emergente"
    Normal = "Normal"

class Solicitud(Base):
    __tablename__ = "tbd_solicitudes"

    ID = Column(Integer, primary_key=True, index=True)
    Paciente_ID = Column(Integer, ForeignKey("tbb_personas.id"))
    Medico_ID = Column(Integer, ForeignKey("tbb_personal_medico.Persona_ID"))
    Servicio_ID = Column(Integer, ForeignKey("tbc_servicios_medicos.ID"))
    Prioridad = Column(Enum(MyPrioridad))
    Descripcion = Column(String(250))
    Estatus = Column(Enum(MyEstatus))
    Estatus_Aprobacion = Column(Boolean, nullable=True)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    # Relaciones
    aprobaciones = relationship("Aprobaciones", back_populates="solicitudes")
    servicio_medico = relationship("ServicioMedico", back_populates="solicitudes")
