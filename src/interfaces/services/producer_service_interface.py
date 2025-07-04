from abc import ABC, abstractmethod


class IProducerService(ABC):
    """Interface for Producer Service."""

    @abstractmethod
    def get_all_producers(self):
        """Retrieve all producers."""
        pass

    @abstractmethod
    def get_producer_by_id(self, producer_id):
        """Retrieve a producer by its ID."""
        pass

    @abstractmethod
    def create_producer(self, producer_data):
        """Create a new producer."""
        pass

    @abstractmethod
    def update_producer(self, producer_id, producer_data):
        """Update an existing producer."""
        pass

    @abstractmethod
    def delete_producer(self, producer_id):
        """Delete a producer by its ID."""
        pass
