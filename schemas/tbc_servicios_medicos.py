# schemas/tbc_servicios_medicos.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ServicioMedicoBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Observaciones: Optional[str] = None

class ServicioMedicoCreate(ServicioMedicoBase):
    pass

class ServicioMedicoUpdate(BaseModel):
    Nombre: Optional[str] = None
    Descripcion: Optional[str] = None
    Observaciones: Optional[str] = None

class ServicioMedico(ServicioMedicoBase):
    ID: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True