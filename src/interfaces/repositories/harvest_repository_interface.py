from abc import ABC, abstractmethod

from models import Harvest
from models.crop import CropType  # Assuming CropType is defined in models.crop

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
