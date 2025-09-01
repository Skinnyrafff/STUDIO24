# STUDIO24

Este es un proyecto de aplicación web para la gestión de un estudio, desarrollado con un backend de FastAPI y un frontend de React.

## Descripción

La aplicación permite gestionar citas y usuarios, con dos vistas principales: una para el propietario/administrador del estudio y otra para los clientes.

### Backend

- **Framework:** FastAPI
- **Base de datos:** La configuración de la base de datos se encuentra en `Backend/database.py`.
- **Modelos:** Los modelos de datos están definidos en `Backend/models.py`.
- **Rutas:**
    - `/users`: Gestión de usuarios.
    - `/appointments`: Gestión de citas.

### Frontend

- **Framework:** React (con Vite)
- **Enrutamiento:** `react-router-dom` para la navegación entre vistas.
- **Vistas:**
    - `OwnerView`: Vista para el administrador.
    - `ClientView`: Vista para los clientes.
- **Componentes:** Incluye componentes reutilizables como un calendario y una lista de usuarios.

## Cómo empezar

### Prerrequisitos

- Python 3.10 o superior
- Node.js y npm

### Backend Setup

1.  Navega al directorio `Backend`:
    ```bash
    cd Backend
    ```
2.  Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```
3.  Activa el entorno virtual:
    - En Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
4.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
5.  Inicia el servidor de desarrollo:
    ```bash
    uvicorn main:app --reload
    ```
El backend estará corriendo en `http://127.0.0.1:8000`.

### Frontend Setup

1.  Navega al directorio `frontend`:
    ```bash
    cd frontend
    ```
2.  Instala las dependencias:
    ```bash
    npm install
    ```
3.  Inicia el servidor de desarrollo:
    ```bash
    npm run dev
    ```
El frontend estará corriendo en `http://localhost:5173`.
