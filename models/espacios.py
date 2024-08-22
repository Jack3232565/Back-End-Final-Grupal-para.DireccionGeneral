from sqlalchemy import Column, Integer, String, Enum, DateTime
from config.db import Base
import enum

class TipoEspacioEnum(str, enum.Enum):
    Consultorio = 'Consultorio'
    Laboratorio = 'Laboratorio'
    Quirófano = 'Quirófano'
    Sala_de_Espera = 'Sala de Espera'
    Edificio = 'Edificio'
    Estacionamiento = 'Estacionamiento'
    Habitación = 'Habitación'
    Cama = 'Cama'
    Sala_Maternidad = 'Sala Maternidad'
    Cunero = 'Cunero'
    Anfiteatro = 'Anfiteatro'
    Oficina = 'Oficina'
    Sala_de_Juntas = 'Sala de Juntas'
    Auditorio = 'Auditorio'
    Cafeteria = 'Cafeteria'
    Capilla = 'Capilla'
    Farmacia = 'Farmacia'
    Ventanilla = 'Ventanilla'
    Recepción = 'Recepción'
    Piso = 'Piso'

class EstatusEnum(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'
    En_remodelación = 'En remodelación'
    Clausurado = 'Clausurado'
    Reubicado = 'Reubicado'
    Temporal = 'Temporal'

class Espacio(Base):
    __tablename__ = 'tbc_espacios'

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Tipo = Column(Enum(TipoEspacioEnum), nullable=False)
    Nombre = Column(String(100), nullable=False)
    Departamento_ID = Column(Integer, nullable=False)
    Estatus = Column(Enum(EstatusEnum), nullable=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Capacidad = Column(Integer)
    Espacio_superior_ID = Column(Integer, nullable=True)
    tbc_espacioscol = Column(String(45), nullable=True)
