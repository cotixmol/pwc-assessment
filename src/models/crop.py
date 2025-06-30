import enum
import uuid
from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from src.models.base import Base


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

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(Enum(CropType), nullable=False)
    brand = Column(String, nullable=False)
