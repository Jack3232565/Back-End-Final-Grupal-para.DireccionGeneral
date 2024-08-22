from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from config.db import Base

class Departamento(Base):
    __tablename__ = "tbc_departamentos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    AreaMedica_ID = Column(Integer, ForeignKey("tbc_areas_medicas.ID"), nullable=True)
    Departamento_Superior_ID = Column(Integer, ForeignKey("tbc_departamentos.id"), nullable=True)
    Responsable_ID = Column(Integer, nullable=True)
    Estatus = Column(Boolean, default=True, nullable=False)
    Fecha_Registro = Column(DateTime, default=datetime.utcnow, nullable=False)
    Fecha_Actualizacion = Column(DateTime, nullable=True)

    departamento_superior = relationship("Departamento", remote_side=[id], back_populates="subdepartamentos")
    subdepartamentos = relationship("Departamento", back_populates="departamento_superior")
    personal_medico = relationship("PersonalMedico", back_populates="departamento")
    area_medica = relationship("AreaMedica", back_populates="departamentos")