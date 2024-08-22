from sqlalchemy.orm import Session
from models import tbb_usuarios as models_tbb_usuarios
from schemas import tbb_usuarios as schemas_tbb_usuarios

def get_tbb_usuario(db: Session, id: int):
    return db.query(models_tbb_usuarios.tbb_usuarios).filter(models_tbb_usuarios.tbb_usuarios.Persona_ID == id).first()

def get_tbb_usuario_by_name(db: Session, nombre: str):
    return db.query(models_tbb_usuarios.tbb_usuarios).filter(models_tbb_usuarios.tbb_usuarios.Nombre_Usuario == nombre).first()


def get_user_by_credentials(db: Session, username: str = None, correo: str = None, telefono: str = None, password: str = None):
    query = db.query(models_tbb_usuarios.tbb_usuarios)
    
    # Filtros de combinación para usuario y contraseña
    if username and password:
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Nombre_Usuario == username)
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Contrasena == password)
    
    # Filtros de combinación para correo y contraseña
    elif correo and password:
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Correo_Electronico == correo)
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Contrasena == password)
    
    # Filtros de combinación para usuario y teléfono
    elif username and telefono:
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Nombre_Usuario == username)
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Numero_Telefonico_Movil == telefono)
    
    # Filtros de combinación para correo y teléfono (opcional)
    elif correo and telefono:
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Correo_Electronico == correo)
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Numero_Telefonico_Movil == telefono)
    
    # Filtros si solo hay un campo con el password
    elif telefono and password:
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Numero_Telefonico_Movil == telefono)
        query = query.filter(models_tbb_usuarios.tbb_usuarios.Contrasena == password)
    
    # Ejecución de la consulta
    user = query.first()
    
    if user:
        return user
    return None


def get_tbb_usuario_by_persona_id(db: Session, persona_id: int):
    return db.query(models_tbb_usuarios.tbb_usuarios).filter(models_tbb_usuarios.tbb_usuarios.Persona_ID == persona_id).first()

def get_all_tbb_usuarios(db: Session):
    return db.query(models_tbb_usuarios.tbb_usuarios).all()

def create_tbb_usuario(db: Session, tbb_usuario: schemas_tbb_usuarios.tbb_usuarioCreate):
    db_usuario = models_tbb_usuarios.tbb_usuarios(
        Persona_ID=tbb_usuario.Persona_ID,
        Nombre_Usuario=tbb_usuario.Nombre_Usuario,
        Correo_Electronico=tbb_usuario.Correo_Electronico,
        Contrasena=tbb_usuario.Contrasena,
        Numero_Telefonico_Movil=tbb_usuario.Numero_Telefonico_Movil,
        Estatus=tbb_usuario.Estatus,
        Fecha_Registro=tbb_usuario.Fecha_Registro,
        Fecha_Actualizacion=tbb_usuario.Fecha_Actualizacion
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_tbb_usuario(db: Session, id: int, tbb_usuario: schemas_tbb_usuarios.tbb_usuarioUpdate):
    db_usuario = db.query(models_tbb_usuarios.tbb_usuarios).filter(models_tbb_usuarios.tbb_usuarios.Persona_ID == id).first()
    if db_usuario:
        for key, value in tbb_usuario.dict(exclude_unset=True).items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_tbb_usuario(db: Session, id: int):
    db_usuario = db.query(models_tbb_usuarios.tbb_usuarios).filter(models_tbb_usuarios.tbb_usuarios.Persona_ID == id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario
