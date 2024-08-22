from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TurnoEnum(str, Enum):
    Mañana = "Mañana"
    Tarde = "Tarde"
    Noche = "Noche"

class PuestoDepartamentoBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Salario: Optional[float] = None
    Turno: Optional[TurnoEnum] = None
    Creado: datetime
    Modificado: Optional[datetime] = None
    DepartamentoID: int

class PuestoDepartamentoCreate(PuestoDepartamentoBase):
    pass

class PuestoDepartamentoUpdate(PuestoDepartamentoBase):
    pass

class PuestoDepartamento(PuestoDepartamentoBase):
    PuestoID: int

    class Config:
        from_attributes = True
