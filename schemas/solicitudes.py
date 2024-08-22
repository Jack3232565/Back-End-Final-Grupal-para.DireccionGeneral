from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from models.solicitudes import MyEstatus, MyPrioridad

class SolicitudBase(BaseModel):
    Paciente_ID: Optional[int]  # Puede ser None si no se proporciona
    Medico_ID: Optional[int]    # Puede ser None si no se proporciona
    Servicio_ID: Optional[int]  # Puede ser None si no se proporciona
    Prioridad: Optional[MyPrioridad]  # Puede ser None si no se proporciona
    Descripcion: Optional[str]  # Puede ser None si no se proporciona
    Estatus: Optional[MyEstatus]  # Puede ser None si no se proporciona
    Estatus_Aprobacion: Optional[bool]  # Puede ser None si no se proporciona
    Fecha_Registro: Optional[datetime]  # Puede ser None si no se proporciona
    Fecha_Actualizacion: Optional[datetime]  # Puede ser None si no se proporciona

class SolicitudCreate(SolicitudBase):
    pass

class SolicitudUpdate(SolicitudBase):
    pass

class Solicitud(SolicitudBase):
    ID: int
    class Config:
        from_attributes = True