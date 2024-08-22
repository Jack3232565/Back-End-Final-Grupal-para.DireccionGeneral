from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, func
from config.db import Base
from sqlalchemy.orm import relationship


class Roles(Base):
    __tablename__ = 'tbc_roles'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(50), nullable=False)
    Descripcion = Column(Text)
    Estatus = Column(Integer, default=1)  # Almacenará 1 (equivalente a b'1') o 0 (equivalente a b'0')
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime, nullable=True, default=None)

    @property
    def estatus(self):
        return self.Estatus == 1

    @estatus.setter
    def estatus(self, value):
        self.Estatus = 1 if value else 0

    usuarios = relationship("UsuarioRoles", back_populates="rol")