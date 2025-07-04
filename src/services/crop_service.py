from dtos import CropCreate, CropRead, CropUpdate
from interfaces.repositories import ICropRepository
from interfaces.services import ICropService


class CropService(ICropService):
    """Service class for managing crop-related business logic."""

    def __init__(self, crop_repository: ICropRepository):
        """Initialize the CropService with a crop repository."""
        self.crop_repository = crop_repository

    def get_all_crops(self) -> list[CropRead]:
        return self.crop_repository.get_all()

    def get_crop_by_id(self, crop_id: int) -> CropRead:
        return self.crop_repository.get_by_id(crop_id)

    def create_crop(self, crop_data: CropCreate) -> CropRead:
        return self.crop_repository.create(crop_data)

    def update_crop(self, crop_id: int, crop_data: CropUpdate) -> CropRead:
        return self.crop_repository.update(crop_id, crop_data)

    def delete_crop(self, crop_id: int) -> bool:
        return self.crop_repository.delete(crop_id)
