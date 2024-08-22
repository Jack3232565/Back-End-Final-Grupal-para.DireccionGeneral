from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class EstatusVidaEnum(str, Enum):
    Vivo = 'Vivo'
    Finado = 'Finado'
    Coma = 'Coma'
    Vegetativo = 'Vegetativo'

class TbbPacientesBase(BaseModel):
    NSS: Optional[str] = None
    Tipo_Seguro: str
    Fecha_Ultima_Cita: Optional[datetime] = None
    Estatus_Medico: Optional[str] = 'Normal'
    Estatus_Vida: EstatusVidaEnum = EstatusVidaEnum.Vivo
    Estatus: Optional[bytes] = b'\x01'
    Fecha_Registro: datetime
    Fecha_Actualizacion: Optional[datetime] = None

class TbbPacientesCreate(TbbPacientesBase):
    Persona_ID: int

class TbbPacientesUpdate(TbbPacientesBase):
    pass

class TbbPacientes(TbbPacientesBase):
    Persona_ID: int

    class Config:
        from_attributes = True