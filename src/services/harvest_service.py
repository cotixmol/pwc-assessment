from dtos import HarvestCreate, HarvestRead, HarvestUpdate
from interfaces.repositories import IHarvestRepository
from interfaces.services import IHarvestService


class HarvestService(IHarvestService):
    """Service class for managing harvest-related business logic."""

    def __init__(self, harvest_repository: IHarvestRepository):
        """Initialize the HarvestService with a harvest repository."""
        self.harvest_repository = harvest_repository

    def get_all_harvests(self) -> list[HarvestRead]:
        return self.harvest_repository.get_all()

    def get_harvest_by_id(self, harvest_id: int) -> HarvestRead:
        return self.harvest_repository.get_by_id(harvest_id)

    def create_harvest(self, harvest_data: HarvestCreate) -> HarvestRead:
        return self.harvest_repository.create(harvest_data)

    def update_harvest(
        self, harvest_id: int, harvest_data: HarvestUpdate
    ) -> HarvestRead:
        return self.harvest_repository.update(harvest_id, harvest_data)

    def delete_harvest(self, harvest_id: int) -> bool:
        return self.harvest_repository.delete(harvest_id)
