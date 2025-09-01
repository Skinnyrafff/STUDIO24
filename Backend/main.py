from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users
from routers import appointments

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:3000",  # Origen del frontend en desarrollo
    "http://localhost:5173",  # Puerto por defecto de Vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(appointments.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Servidor funcionando"}