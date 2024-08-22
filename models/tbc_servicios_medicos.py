from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class ServicioMedico(Base):
    __tablename__ = "tbc_servicios_medicos"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Nombre = Column(String(255), unique=True, nullable=False)
    Descripcion = Column(Text, nullable=True)
    Observaciones = Column(Text, nullable=True)
    Fecha_Registro = Column(DateTime, server_default=func.now(), nullable=False)
    Fecha_Actualizacion = Column(DateTime, onupdate=func.now(), nullable=True)

    solicitudes = relationship("Solicitud", back_populates="servicio_medico")
