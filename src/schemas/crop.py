from pydantic import BaseModel
from typing import Optional
from models import CropType


class CropBase(BaseModel):
    type: CropType
    brand: str


class CropCreate(CropBase):
    pass


class CropRead(CropBase):
    id: int

    class Config:
        orm_mode = True


class CropUpdate(BaseModel):
    type: Optional[CropType] = None
    brand: Optional[str] = None
