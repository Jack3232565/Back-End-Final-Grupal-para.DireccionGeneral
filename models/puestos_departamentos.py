from sqlalchemy import Column, Integer, String, Text, DECIMAL, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class TurnoEnum(str, enum.Enum):
    Mañana = "Mañana"
    Tarde = "Tarde"
    Noche = "Noche"

class PuestoDepartamento(Base):
    __tablename__ = "tbd_puestos_departamentos"

    PuestoID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(100), nullable=False)
    Descripcion = Column(Text, nullable=True)
    Salario = Column(DECIMAL(10, 2), nullable=True)
    Turno = Column(Enum(TurnoEnum), nullable=True)
    Creado = Column(DateTime, nullable=True, default=datetime.utcnow)
    Modificado = Column(DateTime, nullable=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    DepartamentoID = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<PuestoDepartamento(PuestoID={self.PuestoID}, Nombre='{self.Nombre}', Turno='{self.Turno}', DepartamentoID={self.DepartamentoID})>"
