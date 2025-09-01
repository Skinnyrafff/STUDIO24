from database import get_connection
from datetime import datetime
import uuid
def is_valid_hour(date: datetime) -> bool:
    # lunes = 0, domingo = 6
    if date.weekday() > 4:
        return False
    if not (10 <= date.hour < 20):
        return False
    return True

def is_slot_available(date: datetime) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM appointments WHERE date = %s;", (date,))
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count == 0

def create_appointment(user_id: str, date: datetime):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO appointments (user_id, date)
        VALUES (%s, %s)
        RETURNING id;
    """, (user_id, date))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_id

def is_valid_uuid(value: str) -> bool:
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False