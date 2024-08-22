from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    Nombre: str
    Descripcion: str
    Estatus: bool
    Fecha_Registro: Optional[datetime] = None  # Permitir que sea opcional
    Fecha_Actualizacion: Optional[datetime] = None  # Permitir que sea opcional

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    id: int
    
    class Config:
        from_attributes = True

