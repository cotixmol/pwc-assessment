import datetime
from typing import Optional

from pydantic import BaseModel


class HarvestCreate(BaseModel):
    producer_id: int
    crop_id: int
    harvest_date: datetime.date
    quantity_tonnes: float


class HarvestRead(BaseModel):
    id: int
    producer_id: int
    crop_id: int
    harvest_date: datetime.date
    quantity_tonnes: float

    class Config:
        orm_mode = True


class HarvestUpdate(BaseModel):
    producer_id: Optional[int] = None
    crop_id: Optional[int] = None
    harvest_date: Optional[datetime.date] = None
    quantity_tonnes: Optional[float] = None
