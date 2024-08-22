from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class PersonBase(BaseModel):
    Titulo_Cortesia: str
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: Optional[str] = None
    CURP: str
    Fecha_Nacimiento: date
    Genero: str
    Tipo_Sangre: str
    Estatus: bool

class PersonCreate(PersonBase):
    Fotografia: str  # Almacenará la ruta del archivo
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class PersonUpdate(PersonBase):
    Fotografia: Optional[str] = None
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

class Person(PersonBase):
    id: int
    Fotografia: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

    class Config:
        from_attributes = True
