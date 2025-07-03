from pydantic import BaseModel, EmailStr
from typing import Optional


class ProducerCreate(BaseModel):
    name: str
    email: EmailStr


class ProducerRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class ProducerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
