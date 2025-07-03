from interfaces.services import IHarvestService


class HarvestService(IHarvestService):
    def __init__(self, harvest_repository):
        self.harvest_repository = harvest_repository

    def get_all_harvests(self):
        return self.harvest_repository.get_all()

    def get_harvest_by_id(self, id):
        return self.harvest_repository.get_by_id(id)

    def create_harvest(self, harvest_data):
        return self.harvest_repository.create(harvest_data)

    def update_harvest(self, id, harvest_data):
        return self.harvest_repository.update(id, harvest_data)

    def delete_harvest(self, id):
        return self.harvest_repository.delete(id)
