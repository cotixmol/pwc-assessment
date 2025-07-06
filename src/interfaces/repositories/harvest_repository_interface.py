from abc import ABC, abstractmethod

from src.models import Harvest
from src.models.crop import CropType

from .base_repository_interface import IBaseRepository


class IHarvestRepository(IBaseRepository[Harvest], ABC):
    """Repository interface for Harvest-specific methods."""

    @abstractmethod
    def get_total_harvested_by_producer_and_crop_type(
        self, producer_id: int, crop_type: CropType
    ) -> float:
        """
        Calculates the total tonnes of a specific crop type harvested by a producer.
        """
        pass

    @abstractmethod
    async def get_by_crop_id(self, crop_id: int) -> list[Harvest]:
        """Gets all harvests associated with a specific crop ID."""
        pass
