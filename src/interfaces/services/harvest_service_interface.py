from abc import ABC, abstractmethod


class IHarvestService(ABC):
    """
    Interface for Harvest Service.
    """

    @abstractmethod
    def get_all_harvests(self):
        pass

    @abstractmethod
    def get_harvest_by_id(self, id):
        pass

    @abstractmethod
    def create_harvest(self, harvest_data):
        pass

    @abstractmethod
    def update_harvest(self, id, harvest_data):
        pass

    @abstractmethod
    def delete_harvest(self, id):
        pass
