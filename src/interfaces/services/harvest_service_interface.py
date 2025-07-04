from abc import ABC, abstractmethod


class IHarvestService(ABC):
    """Interface for Harvest Service."""

    @abstractmethod
    def get_all_harvests(self):
        """Retrieve all harvests."""
        pass

    @abstractmethod
    def get_harvest_by_id(self, harvest_id):
        """Retrieve a harvest by its ID."""
        pass

    @abstractmethod
    def create_harvest(self, harvest_data):
        """Create a new harvest."""
        pass

    @abstractmethod
    def update_harvest(self, harvest_id, harvest_data):
        """Update an existing harvest."""
        pass

    @abstractmethod
    def delete_harvest(self, harvest_id):
        """Delete a harvest by its ID."""
        pass
