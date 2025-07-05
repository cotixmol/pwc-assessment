from abc import ABC, abstractmethod

from models.crop import CropType


class IStockService(ABC):
    """Interface for Stock Service."""

    @abstractmethod
    async def get_available_stock(self, producer_id: int, crop_type: CropType) -> float:
        """Calculates the available stock for a producer and a specific crop type."""
        pass
