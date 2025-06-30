import datetime
import uuid
from sqlalchemy import Column, Date, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from src.models.base import Base


class Harvest(Base):
    """
    Links to the specific Crop product that was harvested by a Producer.
    """

    __tablename__ = "harvests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    producer_id = Column(UUID(as_uuid=True), ForeignKey("producers.id"), nullable=False)
    crop_id = Column(UUID(as_uuid=True), ForeignKey("crops.id"), nullable=False)
    harvest_date = Column(Date, default=datetime.date.today, nullable=False)
    quantity_tonnes = Column(Float, nullable=False)
