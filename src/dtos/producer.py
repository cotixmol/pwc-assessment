from typing import Optional

from pydantic import BaseModel, EmailStr


class ProducerCreate(BaseModel):
    name: str
    email: EmailStr


class ProducerRead(BaseModel):
    name: str
    email: EmailStr
    id: int

    class Config:
        orm_mode = True


class ProducerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
