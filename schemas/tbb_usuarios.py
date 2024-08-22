from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class tbb_usuarioBase(BaseModel):
    Persona_ID: int
    Nombre_Usuario: str
    Correo_Electronico: str
    Numero_Telefonico_Movil: str
    Contrasena: str
    Estatus: str

class tbb_usuarioCreate(tbb_usuarioBase):
    Fecha_Registro: datetime
    Fecha_Actualizacion: Optional[datetime] = None

class tbb_usuarioUpdate(tbb_usuarioBase):
    Fecha_Actualizacion: datetime

class tbb_usuario(tbb_usuarioBase):
    ID: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    Nombre_Usuario: str
    Correo_Electronico: str
    Numero_Telefonico_Movil: str
    Contrasena: str


class UserLoginResponse(BaseModel):
    token: str
    mensaje: str
