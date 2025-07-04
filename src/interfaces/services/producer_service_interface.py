from abc import ABC, abstractmethod

from schemas import ProducerCreate, ProducerRead, ProducerUpdate


class IProducerService(ABC):
    """Interface for Producer Service."""

    @abstractmethod
    def get_all_producers(self) -> list[ProducerRead]:
        """Retrieve all producers."""
        pass

    @abstractmethod
    def get_producer_by_id(self, producer_id: int) -> ProducerRead:
        """Retrieve a producer by its ID."""
        pass

    @abstractmethod
    def create_producer(self, producer_data: ProducerCreate) -> ProducerRead:
        """Create a new producer."""
        pass

    @abstractmethod
    def update_producer(
        self, producer_id: int, producer_data: ProducerUpdate
    ) -> ProducerRead:
        """Update an existing producer."""
        pass

    @abstractmethod
    def delete_producer(self, producer_id: int) -> bool:
        """Delete a producer by its ID."""
        pass
