import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, PositiveFloat

from src.models.crop import CropType


class SaleCreate(BaseModel):
    producer_id: int
    crop_type: CropType
    sale_date: datetime.date
    quantity_sold: PositiveFloat
    price_per_tonne: PositiveFloat


class SaleRead(BaseModel):
    id: int
    producer_id: int
    crop_type: CropType
    sale_date: datetime.date
    quantity_sold: PositiveFloat
    price_per_tonne: PositiveFloat
    available_stock: Optional[PositiveFloat] = None

    model_config = ConfigDict(from_attributes=True)


class SaleUpdate(BaseModel):
    sale_date: Optional[datetime.date] = None
    quantity_sold: Optional[PositiveFloat] = None
    price_per_tonne: Optional[PositiveFloat] = None
