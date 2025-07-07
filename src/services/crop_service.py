from src.dtos import CropCreate, CropRead, CropUpdate
from src.exceptions import CropNotFoundError, DeletionError
from src.interfaces.repositories import (
    ICropRepository,
    IHarvestRepository,
    ISaleRepository,
)
from src.interfaces.services import ICropService


class CropService(ICropService):
    """Service class for managing crop-related business logic."""

    def __init__(
        self,
        crop_repository: ICropRepository,
        harvest_repository: IHarvestRepository,
        sale_repository: ISaleRepository,
    ):
        """Initialize the CropService with a crop repository."""
        self.crop_repository = crop_repository
        self.harvest_repository = harvest_repository
        self.sale_repository = sale_repository

    async def get_all_crops(self) -> list[CropRead]:
        return await self.crop_repository.get_all()

    async def get_crop_by_id(self, crop_id: int) -> CropRead:
        crop = await self.crop_repository.get_by_id(crop_id)
        if not crop:
            raise CropNotFoundError(crop_id)
        return crop

    async def create_crop(self, crop_data: CropCreate) -> CropRead:
        return await self.crop_repository.create(crop_data.model_dump())

    async def update_crop(self, crop_id: int, crop_data: CropUpdate) -> CropRead:
        updated_crop = await self.crop_repository.update(
            crop_id, crop_data.model_dump(exclude_unset=True)
        )
        if not updated_crop:
            raise CropNotFoundError(crop_id)
        return updated_crop

    async def delete_crop(self, crop_id: int) -> bool:
        crop_to_delete = await self.crop_repository.get_by_id(crop_id)
        if not crop_to_delete:
            raise CropNotFoundError(crop_id)

        related_harvests = await self.harvest_repository.get_by_crop_id(crop_id)
        if related_harvests:
            raise DeletionError(
                f"Crop ID: {crop_id} cannot be deleted. It is used in {len(related_harvests)} harvest(s)."
            )

        sales_of_type = await self.sale_repository.get_by_crop_type(crop_to_delete.type)
        if sales_of_type:
            raise DeletionError(
                f"Crop ID: {crop_id} cannot be deleted. The crop type '{crop_to_delete.type.value}' is used in {len(sales_of_type)} sale(s)."
            )

        deleted = await self.crop_repository.delete(crop_id)

        return deleted
