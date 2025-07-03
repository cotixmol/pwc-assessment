from pydantic import BaseModel, EmailStr
from typing import Optional


class ProducerBase(BaseModel):
    name: str
    email: EmailStr


class ProducerCreate(ProducerBase):
    pass


class ProducerRead(ProducerBase):
    id: int

    class Config:
        orm_mode = True


class ProducerUpdate(ProducerBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
