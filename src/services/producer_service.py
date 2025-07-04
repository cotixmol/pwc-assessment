from interfaces.services import IProducerService


class ProducerService(IProducerService):
    """Service class for managing producer-related operations."""

    def __init__(self, producer_repository):
        """Initialize the ProducerService with a producer repository."""
        self.producer_repository = producer_repository

    def get_all_producers(self):
        return self.producer_repository.get_all()

    def get_producer_by_id(self, producer_id):
        return self.producer_repository.get_by_id(producer_id)

    def create_producer(self, producer_data):
        return self.producer_repository.create(producer_data)

    def update_producer(self, producer_id, producer_data):
        return self.producer_repository.update(producer_id, producer_data)

    def delete_producer(self, producer_id):
        return self.producer_repository.delete(producer_id)
