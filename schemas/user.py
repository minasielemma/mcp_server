from pydantic import BaseModel
from typing import Optional, Dict

class UserCreate(BaseModel):
    email: str
    password: str

class UserRead(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True

class EmailAnalysisCreate(BaseModel):
    email_id: str
    sender: str
    subject: str
    body: str
    user_id:Optional[str] = None
    analysis: Optional[Dict] = None

class EmailAnalysisRead(EmailAnalysisCreate):
    id: int
    created_at: str
    user_id: str

    class Config:
        orm_mode = True
