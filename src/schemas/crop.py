from typing import Optional

from models import CropType
from pydantic import BaseModel


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
