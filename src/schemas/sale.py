from pydantic import BaseModel
from typing import Optional
import datetime


class SaleBase(BaseModel):
    harvest_id: int
    sale_date: datetime.date
    quantity_sold: float
    price_per_tonne: float


class SaleCreate(SaleBase):
    pass


class SaleRead(SaleBase):
    id: int

    class Config:
        orm_mode = True


class SaleUpdate(BaseModel):
    harvest_id: Optional[int] = None
    sale_date: Optional[datetime.date] = None
    quantity_sold: Optional[float] = None
    price_per_tonne: Optional[float] = None
