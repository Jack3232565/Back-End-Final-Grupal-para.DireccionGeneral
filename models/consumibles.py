from sqlalchemy import Column, Integer, String, Enum, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base
import enum

class EstatusEnum(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    En_Revisión = "En Revisión"

class Consumible(Base):
    __tablename__ = "tbc_consumibles"
    
    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Nombre = Column(String(255), nullable=False)
    Descripcion = Column(Text, nullable=True)
    Cantidad = Column(Integer, nullable=False)
    Tipo = Column(String(50), nullable=False)
    Departamento_ID = Column(Integer, nullable=False)
    Estatus = Column(Enum(EstatusEnum), default=EstatusEnum.Activo, nullable=False)
    Fecha_Registro = Column(DateTime, nullable=True, default=func.now())
    Fecha_Actualizacion = Column(DateTime, nullable=True, default=func.now(), onupdate=func.now())
    Observaciones = Column(Text, nullable=True)
    Espacio_Medico = Column(String(50), nullable=False)

