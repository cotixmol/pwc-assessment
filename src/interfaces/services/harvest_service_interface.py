from abc import ABC, abstractmethod

from schemas import HarvestCreate, HarvestRead, HarvestUpdate


class IHarvestService(ABC):
    """Interface for Harvest Service."""

    @abstractmethod
    def get_all_harvests(self) -> list[HarvestRead]:
        """Retrieve all harvests."""
        pass

    @abstractmethod
    def get_harvest_by_id(self, harvest_id: int) -> HarvestRead:
        """Retrieve a harvest by its ID."""
        pass

    @abstractmethod
    def create_harvest(self, harvest_data: HarvestCreate) -> HarvestRead:
        """Create a new harvest."""
        pass

    @abstractmethod
    def update_harvest(
        self, harvest_id: int, harvest_data: HarvestUpdate
    ) -> HarvestRead:
        """Update an existing harvest."""
        pass

    @abstractmethod
    def delete_harvest(self, harvest_id: int) -> bool:
        """Delete a harvest by its ID."""
        pass
