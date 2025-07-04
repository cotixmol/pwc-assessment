from abc import ABC, abstractmethod

from schemas import CropCreate, CropRead, CropUpdate


class ICropService(ABC):
    """Interface for Crop Service."""

    @abstractmethod
    def get_all_crops(self) -> list[CropRead]:
        """Retrieve all crops."""
        pass

    @abstractmethod
    def get_crop_by_id(self, crop_id: int) -> CropRead:
        """Retrieve a crop by its ID."""
        pass

    @abstractmethod
    def create_crop(self, crop_data: CropCreate) -> CropRead:
        """Create a new crop."""
        pass

    @abstractmethod
    def update_crop(self, crop_id: int, crop_data: CropUpdate) -> CropRead:
        """Update an existing crop."""
        pass

    @abstractmethod
    def delete_crop(self, crop_id: int) -> bool:
        """Delete a crop by its ID."""
        pass
