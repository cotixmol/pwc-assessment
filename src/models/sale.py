import datetime
import uuid
from sqlalchemy import Column, Date, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from src.models.base import Base


class Sale(Base):
    """
    Represents a transaction where a certain quantity of a harvest is sold.
    """

    __tablename__ = "sales"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    harvest_id = Column(UUID(as_uuid=True), ForeignKey("harvests.id"), nullable=False)
    sale_date = Column(Date, default=datetime.date.today, nullable=False)
    quantity_sold = Column(Float, nullable=False)
    price_per_tonne = Column(Float, nullable=False)
