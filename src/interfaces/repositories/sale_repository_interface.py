from abc import ABC, abstractmethod

from src.models import Sale
from src.models.crop import CropType

from .base_repository_interface import IBaseRepository


class ISaleRepository(IBaseRepository[Sale], ABC):
    """Repository interface for Sale-specific methods."""

    @abstractmethod
    def get_total_sold_by_producer_and_crop_type(
        self, producer_id: int, crop_type: CropType
    ) -> float:
        """
        Calculates the total tonnes of a specific crop type sold by a producer.
        """
        pass

    @abstractmethod
    async def get_by_crop_type(self, crop_type: CropType) -> list[Sale]:
        """Gets all sales associated with a specific crop ID."""
        pass
