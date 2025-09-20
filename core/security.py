from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from core.config import FASTAPI_SECRET_KEY, JWT_ALGORITHM

security = HTTPBearer()

def create_jwt(user_id: int):
    return jwt.encode({"user_id": user_id}, FASTAPI_SECRET_KEY, algorithm=JWT_ALGORITHM)

def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, FASTAPI_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    return verify_jwt(token)
