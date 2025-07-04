import datetime

from sqlalchemy import Column, Date, Float, ForeignKey, Integer

from .base import Base


class Harvest(Base):
    """Links to the specific Crop product that was harvested by a Producer."""

    __tablename__ = "harvests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    producer_id = Column(Integer, ForeignKey("producers.id"), nullable=False)
    crop_id = Column(Integer, ForeignKey("crops.id"), nullable=False)
    harvest_date = Column(Date, default=datetime.date.today, nullable=False)
    quantity_tonnes = Column(Float, nullable=False)
