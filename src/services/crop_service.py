from src.dtos import CropCreate, CropRead, CropUpdate
from src.exceptions import CropNotFoundError
from src.interfaces.repositories import ICropRepository
from src.interfaces.services import ICropService


class CropService(ICropService):
    """Service class for managing crop-related business logic."""

    def __init__(self, crop_repository: ICropRepository):
        """Initialize the CropService with a crop repository."""
        self.crop_repository = crop_repository

    def get_all_crops(self) -> list[CropRead]:
        return self.crop_repository.get_all()

    async def get_crop_by_id(self, crop_id: int) -> CropRead:
        crop = await self.crop_repository.get_by_id(crop_id)
        if not crop:
            raise CropNotFoundError(crop_id)
        return crop

    def create_crop(self, crop_data: CropCreate) -> CropRead:
        return self.crop_repository.create(crop_data.model_dump())

    async def update_crop(self, crop_id: int, crop_data: CropUpdate) -> CropRead:
        updated_crop = await self.crop_repository.update(
            crop_id, crop_data.model_dump(exclude_unset=True)
        )
        if not updated_crop:
            raise CropNotFoundError(crop_id)
        return updated_crop

    async def delete_crop(self, crop_id: int) -> bool:
        deleted = await self.crop_repository.delete(crop_id)
        if not deleted:
            raise CropNotFoundError(crop_id)
        return deleted
