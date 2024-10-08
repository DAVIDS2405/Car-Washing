from dotenv import load_dotenv
from fastapi import HTTPException, status
from jose import jwt, JWTError, ExpiredSignatureError
import os
from datetime import datetime, timedelta, UTC

load_dotenv()

ALGORITHM = os.environ.get("ALGORITHM")
SECRET_KEY = os.environ.get("SECRET_KEY")


def create_token(id: str, rol: str = "user"):

    access_token_expires = timedelta(minutes=30)

    expire = datetime.now(UTC) + access_token_expires

    access_token = {"user_id": str(id), "rol": rol, "exp": expire}

    JWT = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)

    return JWT


def validate_token(token: str):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

        return payload

    except ExpiredSignatureError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El Token ha expirado.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Token inválido.",
            headers={"WWW-Authenticate": "Bearer"}
        )


async def verify_rol_user(token: str):

    payload = validate_token(token)

    if payload["rol"] != "user":
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="No tienes permisos para acceder a este recurso."
        )

    return payload["user_id"]


async def verify_rol_admin(token: str):

    payload = validate_token(token)

    if payload["rol"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="No tienes permisos para acceder a este recurso."
        )

    return payload["user_id"]
