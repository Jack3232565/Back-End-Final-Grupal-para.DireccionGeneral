from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class EstatusEnum(str, Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"

class AreaMedicaBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Estatus: EstatusEnum
    Fecha_Registro: datetime
    Fecha_Actualizacion: Optional[datetime] = None

class AreaMedicaCreate(AreaMedicaBase):
    pass

class AreaMedicaUpdate(AreaMedicaBase):
    pass

class AreaMedica(AreaMedicaBase):
    ID: int

    class Config:
        from_attributes = True
