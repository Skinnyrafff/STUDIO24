
from fastapi import APIRouter
from fastapi import HTTPException
from models import LoginRequest
from services.user_service import get_user_by_credentials
from models import RegisterUser
from services.user_service import (
    test_db_service,
    register_user_service,
    list_users_service
)

router = APIRouter(tags=["Users"])

@router.get("/test-db")
def test_db():
    return test_db_service()

@router.post("/register")
def register_user(user: RegisterUser):
    return register_user_service(user)

@router.get("/users")
def list_users():
    return list_users_service()

@router.post("/login")
def login_user(credentials: LoginRequest):
    user = get_user_by_credentials(credentials.email, credentials.phone)
    
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return {
        "message": "Login exitoso",
        "user_id": user["id"],
        "auth_provider": user["auth_provider"]
    }