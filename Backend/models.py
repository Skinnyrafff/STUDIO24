from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class RegisterUser(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    auth_provider: Optional[str] = "manual"  # manual | google | phone

class LoginRequest(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class AppointmentRequest(BaseModel):
    user_id: str
    date: datetime  # fecha + hora exacta (ej: 2024-07-22T15:00)