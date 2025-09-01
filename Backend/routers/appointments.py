import uuid
from fastapi import APIRouter, HTTPException
from models import AppointmentRequest
from services.appointment_service import create_appointment, is_slot_available, is_valid_hour

router = APIRouter(tags=["Appointments"])

def is_valid_uuid(value: str) -> bool:
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False

@router.post("/appointments")
def schedule_appointment(req: AppointmentRequest):
    if not is_valid_hour(req.date):
        raise HTTPException(status_code=400, detail="Horario no válido. Solo se aceptan citas de lunes a viernes entre 10:00 y 20:00.")

    if not is_slot_available(req.date):
        raise HTTPException(status_code=409, detail="Ese horario ya está ocupado.")
    
    if not is_valid_uuid(req.user_id):
        raise HTTPException(status_code=400, detail="user_id inválido")

    appt_id = create_appointment(req.user_id, req.date)
    return {
        "message": "Cita agendada correctamente",
        "appointment_id": appt_id
    }
