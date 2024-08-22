from pydantic import BaseModel
from typing import Optional
import datetime

class EspacioBase(BaseModel):
    Tipo: str
    Nombre: str
    Departamento_ID: int
    Estatus: str
    Capacidad: Optional[int] = None
    Espacio_superior_ID: Optional[int] = None
    tbc_espacioscol: Optional[str] = None

class EspacioCreate(EspacioBase):
    pass

class EspacioUpdate(EspacioBase):
    pass

class Espacio(EspacioBase):
    ID: int
    Fecha_Registro: datetime.datetime
    Fecha_Actualizacion: datetime.datetime
    class Config:
        from_attributes = True  
