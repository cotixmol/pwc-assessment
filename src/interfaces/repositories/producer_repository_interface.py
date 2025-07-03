from abc import ABC, abstractmethod
from models import Producer


class IProducerRepository(ABC):
    """
    Interface for Producer Repository
    """

    @abstractmethod
    async def get_all_producers(self) -> list[Producer]:
        """Retrieves all producers."""
        pass

    @abstractmethod
    async def get_producer_by_id(self, producer_id: int) -> Producer | None:
        """Retrieves a producer by its primary key."""
        pass

    @abstractmethod
    async def create_producer(self, producer_data: dict) -> Producer:
        """Creates and returns a new producer."""
        pass

    @abstractmethod
    async def update_producer(
        self, producer_id: int, producer_data: dict
    ) -> Producer | None:
        """Updates an existing producer."""
        pass

    @abstractmethod
    async def delete_producer(self, producer_id: int) -> bool:
        """Deletes a producer by its ID."""
        pass
