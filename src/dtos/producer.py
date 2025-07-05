from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class ProducerCreate(BaseModel):
    name: str
    email: EmailStr


class ProducerRead(BaseModel):
    name: str
    email: EmailStr
    id: int

    model_config = ConfigDict(from_attributes=True)


class ProducerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
