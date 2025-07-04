from typing import Optional

from models import CropType
from pydantic import BaseModel


class CropCreate(BaseModel):
    type: CropType
    brand: str


class CropRead(BaseModel):
    id: int
    type: CropType
    brand: str

    class Config:
        orm_mode = True


class CropUpdate(BaseModel):
    type: Optional[CropType] = None
    brand: Optional[str] = None
