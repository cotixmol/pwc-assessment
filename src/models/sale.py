import datetime

from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer

from .base import Base
from .crop import CropType


class Sale(Base):
    """Represents a transaction where a certain quantity of a harvest is sold."""

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    producer_id = Column(Integer, ForeignKey("producers.id"), nullable=False)
    crop_type = Column(Enum(CropType), nullable=False)
    quantity_sold = Column(Float, nullable=False)
    price_per_tonne = Column(Float, nullable=False)
    sale_date = Column(Date, default=datetime.date.today, nullable=False)
