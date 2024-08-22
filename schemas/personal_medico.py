from typing import List, Union, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from models.personal_medico import EnumTipoPersonal, EnumEstatus

class PersonalMedicoBase(BaseModel):
    Persona_ID: int
    Departamento_ID: int
    Cedula_Profesional: str
    Tipo: EnumTipoPersonal
    Especialidad: Optional[str] = None  # Este campo ahora es opcional
    Fecha_Registro: datetime
    Fecha_Contratacion: datetime
    Fecha_Termino_Contrato: Optional[datetime] = None  # Este campo ahora es opcional
    Salario: Decimal
    Estatus: EnumEstatus
    Fecha_Actualizacion: Optional[datetime] = None  # Este campo ahora es opcional

class PersonalMedicoCreate(PersonalMedicoBase):
    pass

class PersonalMedicoUpdate(PersonalMedicoBase):
    pass

class PersonalMedico(PersonalMedicoBase):
    Persona_ID: int

    class Config:
        from_attributes = True