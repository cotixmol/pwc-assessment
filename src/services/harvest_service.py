from src.dtos import HarvestCreate, HarvestRead, HarvestUpdate
from src.exceptions import HarvestNotFoundError
from src.interfaces.repositories import IHarvestRepository
from src.interfaces.services import IHarvestService


class HarvestService(IHarvestService):
    """Service class for managing harvest-related business logic."""

    def __init__(self, harvest_repository: IHarvestRepository):
        """Initialize the HarvestService with a harvest repository."""
        self.harvest_repository = harvest_repository

    async def get_all_harvests(self) -> list[HarvestRead]:
        return await self.harvest_repository.get_all()

    async def get_harvest_by_id(self, harvest_id: int) -> HarvestRead:
        harvest = await self.harvest_repository.get_by_id(harvest_id)
        if not harvest:
            raise HarvestNotFoundError(harvest_id)
        return harvest

    async def create_harvest(self, harvest_data: HarvestCreate) -> HarvestRead:
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
        deleted = await self.harvest_repository.delete(harvest_id)
        if not deleted:
            raise HarvestNotFoundError(harvest_id)
        return deleted
