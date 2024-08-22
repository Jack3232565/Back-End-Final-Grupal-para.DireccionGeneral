from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class Rol(Base):
    __tablename__ = "tbc_roles"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(60))
    Descripcion = Column(LONGTEXT)
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime, nullable=False, default=func.now())
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=func.now())

