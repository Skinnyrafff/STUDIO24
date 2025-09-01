
from database import get_connection
from fastapi import HTTPException
from models import RegisterUser

def test_db_service():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return {"users_total": result[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def register_user_service(user: RegisterUser):
    try:
        if not user.email and not user.phone:
            raise HTTPException(status_code=400, detail="Debe proporcionar un email o número de teléfono.")

        conn = get_connection()
        cur = conn.cursor()

        # Validar si ya existe usuario con ese email o teléfono
        cur.execute("""
            SELECT id FROM users WHERE email = %s OR phone = %s;
        """, (user.email, user.phone))
        existing = cur.fetchone()

        if existing:
            cur.close()
            conn.close()
            raise HTTPException(status_code=409, detail="El usuario ya existe.")

        # Insertar nuevo usuario
        cur.execute("""
            INSERT INTO users (name, email, phone, auth_provider)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (user.name, user.email, user.phone, user.auth_provider))
        
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return {"message": "Usuario registrado exitosamente", "user_id": user_id}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def list_users_service():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email, phone, auth_provider, created_at FROM users;")
        users = cur.fetchall()
        cur.close()
        conn.close()

        # Convertir los resultados en lista de diccionarios
        return [
            {
                "id": str(u[0]),
                "name": u[1],
                "email": u[2],
                "phone": u[3],
                "auth_provider": u[4],
                "created_at": u[5].isoformat()
            }
            for u in users
        ]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_user_by_credentials(email=None, phone=None):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT id, auth_provider FROM users
        WHERE email = %s OR phone = %s
    """, (email, phone))
    
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return {
            "id": str(row[0]),
            "auth_provider": row[1]
        }
    