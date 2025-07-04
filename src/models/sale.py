import datetime

from sqlalchemy import Column, Date, Float, ForeignKey, Integer

from .base import Base


class Sale(Base):
    """
    Represents a transaction where a certain quantity of a harvest is sold.
    """

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    harvest_id = Column(Integer, ForeignKey("harvests.id"), nullable=False)
    sale_date = Column(Date, default=datetime.date.today, nullable=False)
    quantity_sold = Column(Float, nullable=False)
    price_per_tonne = Column(Float, nullable=False)
