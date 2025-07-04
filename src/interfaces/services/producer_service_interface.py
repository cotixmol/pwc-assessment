from abc import ABC, abstractmethod


class IProducerService(ABC):
    """
    Interface for Producer Service.
    """

    @abstractmethod
    def get_all_producers(self):
        pass

    @abstractmethod
    def get_producer_by_id(self, id):
        pass

    @abstractmethod
    def create_producer(self, producer_data):
        pass

    @abstractmethod
    def update_producer(self, id, producer_data):
        pass

    @abstractmethod
    def delete_producer(self, id):
        pass
