from interfaces.services import IHarvestService


class HarvestService(IHarvestService):
    """Service class for managing harvest-related operations."""

    def __init__(self, harvest_repository):
        """Initialize the HarvestService with a harvest repository."""
        self.harvest_repository = harvest_repository

    def get_all_harvests(self):
        return self.harvest_repository.get_all()

    def get_harvest_by_id(self, harvest_id):
        return self.harvest_repository.get_by_id(harvest_id)

    def create_harvest(self, harvest_data):
        return self.harvest_repository.create(harvest_data)

    def update_harvest(self, harvest_id, harvest_data):
        return self.harvest_repository.update(harvest_id, harvest_data)

    def delete_harvest(self, harvest_id):
        return self.harvest_repository.delete(harvest_id)
