import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, PositiveFloat


class HarvestCreate(BaseModel):
    producer_id: int
    crop_id: int
    harvest_date: datetime.date
    quantity_tonnes: PositiveFloat


class HarvestRead(BaseModel):
    id: int
    producer_id: int
    crop_id: int
    harvest_date: datetime.date
    quantity_tonnes: PositiveFloat

    model_config = ConfigDict(from_attributes=True)


class HarvestUpdate(BaseModel):
    harvest_date: Optional[datetime.date] = None
    quantity_tonnes: Optional[PositiveFloat] = None
