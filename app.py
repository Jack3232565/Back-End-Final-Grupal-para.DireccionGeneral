from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # Importa StaticFiles
import logging

from routes.user import user
from routes.persons import person
from routes.rol import rol
from routes.userrol import userrol
from routes.cirugia import cirugia_router
from routes.horarios import horarios
from routes.espacios import espacio
from routes.areas_medicas import area_medica
from routes.bitacora import bitacora
from routes.consumibles import consumible
from routes.dispensaciones import dispensacion
from routes.estudios import estudios
from routes.resultados_estudios import resultados_estudios
from routes.lotes import lote
from routes.medicamentos import medicamento
from routes.puestos import puesto
from routes.puestos_departamentos import puesto_departamento
from routes.tbc_servicios_medicos import servicios_medicos
from routes.tbc_departamentos import departamentos  
from routes.personal_medico import personal_medico
from routes.tbb_pacientes import tbb_pacientes
from routes.solicitudes import request
from routes.tbb_aprobaciones import tbb_aprobaciones
from routes.tbc_organos import tbc_organos
from routes.Pediatria.nacimientos import baby
from routes.Pediatria.viewCiudad import view1
from routes.Pediatria.viewGenero import view2


app = FastAPI(
    title="HOSPITAL PrivilegeCare"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes de origen cruzado. Puedes especificar una lista de dominios permitidos.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)


app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(cirugia_router)
app.include_router(horarios)
app.include_router(espacio)
app.include_router(area_medica)
app.include_router(bitacora)
app.include_router(consumible)
app.include_router(dispensacion)
app.include_router(estudios)
app.include_router(resultados_estudios)
app.include_router(lote)
app.include_router(medicamento)
app.include_router(servicios_medicos)
app.include_router(departamentos)
app.include_router(personal_medico)
app.include_router(tbb_pacientes)
app.include_router(puesto)
app.include_router(puesto_departamento)
app.include_router(request)
app.include_router(tbb_aprobaciones)
app.include_router(tbc_organos)
app.include_router(baby)
app.include_router(view1)
app.include_router(view2)

# Configurar el directorio de archivos estáticos
app.mount("/uploads", StaticFiles(directory="uploads", html=False), name="uploads")

# Mensaje de bienvenida usando logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(" Bienvenido al Back-End del Hospital PrivilegeCare")


