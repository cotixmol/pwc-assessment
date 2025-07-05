from typing import Optional

from models import CropType
from pydantic import BaseModel, ConfigDict


class CropCreate(BaseModel):
    type: CropType
    brand: str


class CropRead(BaseModel):
    id: int
    type: CropType
    brand: str

    model_config = ConfigDict(from_attributes=True)


class CropUpdate(BaseModel):
    type: Optional[CropType] = None
    brand: Optional[str] = None
