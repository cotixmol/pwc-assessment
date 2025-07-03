from pydantic import BaseModel
from typing import Optional
import datetime


class HarvestBase(BaseModel):
    producer_id: int
    crop_id: int
    harvest_date: datetime.date
    quantity_tonnes: float


class HarvestCreate(HarvestBase):
    pass


class HarvestRead(HarvestBase):
    id: int

    class Config:
        orm_mode = True


class HarvestUpdate(BaseModel):
    producer_id: Optional[int] = None
    crop_id: Optional[int] = None
    harvest_date: Optional[datetime.date] = None
    quantity_tonnes: Optional[float] = None
