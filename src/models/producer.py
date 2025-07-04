from sqlalchemy import Column, Integer, String

from .base import Base


class Producer(Base):
    """
    Represents the farmer or agricultural entity that produces and sells the harvest.
    """

    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
