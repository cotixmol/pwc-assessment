import enum

from sqlalchemy import Column, Enum, Integer, String

from .base import Base


class CropType(str, enum.Enum):
    """Enumeration for the high-level crop types."""

    SOYBEAN = "soybean"
    WHEAT = "wheat"
    SUNFLOWER = "sunflower"
    CORN = "corn"
    SORGHUM = "sorghum"


class Crop(Base):
    """
    Defines a specific agricultural product with a fixed type and brand.
    """

    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum(CropType), nullable=False)
    brand = Column(String, nullable=False)
