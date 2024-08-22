from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

#se esta entrando en la base de datos con usuario: root y contraseña: 1234, en el puerto de conexion de MySQL 3306
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Probar la conexión
try:
   connection = engine.connect()
   print("Conexión exitosa a la base de datos Remota")
   connection.close()
except Exception as e:
   print(f"Error al conectar a la base de datos: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
