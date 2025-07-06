from src.dtos import HarvestCreate, HarvestRead, HarvestUpdate
from src.exceptions import (
    CropNotFoundError,
    DeletionError,
    HarvestNotFoundError,
    ProducerNotFoundError,
)
from src.interfaces.repositories import (
    ICropRepository,
    IHarvestRepository,
    IProducerRepository,
    ISaleRepository,
)
from src.interfaces.services import IHarvestService


class HarvestService(IHarvestService):
    """Service class for managing harvest-related business logic."""

    def __init__(
        self,
        harvest_repository: IHarvestRepository,
        crop_repository: ICropRepository,
        sale_repository: ISaleRepository,
        producer_repository: IProducerRepository,
    ):
        """Initialize the HarvestService with a harvest repository."""
        self.harvest_repository = harvest_repository
        self.crop_repository = crop_repository
        self.sale_repository = sale_repository
        self.producer_repository = producer_repository

    async def get_all_harvests(self) -> list[HarvestRead]:
        return await self.harvest_repository.get_all()

    async def get_harvest_by_id(self, harvest_id: int) -> HarvestRead:
        harvest = await self.harvest_repository.get_by_id(harvest_id)
        if not harvest:
            raise HarvestNotFoundError(harvest_id)
        return harvest

    async def create_harvest(self, harvest_data: HarvestCreate) -> HarvestRead:
        producer = await self.producer_repository.get_by_id(harvest_data.producer_id)
        if not producer:
            raise ProducerNotFoundError(harvest_data.producer_id)
        crop_to_delete = await self.crop_repository.get_by_id(harvest_data.crop_id)
        if not crop_to_delete:
            raise CropNotFoundError(harvest_data.crop_id)
        return await self.harvest_repository.create(harvest_data.model_dump())

    async def update_harvest(
        self, harvest_id: int, harvest_data: HarvestUpdate
    ) -> HarvestRead:
        updated_harvest = await self.harvest_repository.update(
            harvest_id, harvest_data.model_dump(exclude_unset=True)
        )
        if not updated_harvest:
            raise HarvestNotFoundError(harvest_id)
        return updated_harvest

    async def delete_harvest(self, harvest_id: int) -> bool:
        harvest_to_delete = await self.harvest_repository.get_by_id(harvest_id)
        if not harvest_to_delete:
            raise HarvestNotFoundError(harvest_id)

        crop = await self.crop_repository.get_by_id(harvest_to_delete.crop_id)
        if not crop:
            raise CropNotFoundError(harvest_to_delete.crop_id)
        crop_type = crop.type

        total_harvested = (
            await self.harvest_repository.get_total_harvested_by_producer_and_crop_type(
                harvest_to_delete.producer_id, crop_type
            )
        )
        total_sold = (
            await self.sale_repository.get_total_sold_by_producer_and_crop_type(
                harvest_to_delete.producer_id, crop_type
            )
        )

        if total_sold > (total_harvested - harvest_to_delete.quantity_tonnes):
            raise DeletionError(
                f"Harvest ID: {harvest_id} cannot be deleted. Deleting this would result in a negative stock balance for {crop_type.value}."
            )

        deleted = await self.harvest_repository.delete(harvest_id)

        return deleted
