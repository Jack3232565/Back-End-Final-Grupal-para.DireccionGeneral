from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class DepartamentoBase(BaseModel):
    Nombre: str = Field(..., description="Denominación del departamento")
    AreaMedica_ID: Optional[int] = Field(None, description="ID del área médica")
    Departamento_Superior_ID: Optional[int] = Field(None, description="ID del departamento superior")
    Responsable_ID: Optional[int] = Field(None, description="ID del responsable del departamento")
    Estatus: bool = Field(True, description="Estatus del departamento")  # Se eliminó `...` para evitar duplicado
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

class DepartamentoCreate(DepartamentoBase):
    pass

class DepartamentoUpdate(DepartamentoBase):
    pass

class Departamento(DepartamentoBase):
    id: int

    class Config:
        from_attributes = True