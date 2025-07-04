from interfaces.repositories import IProducerRepository
from interfaces.services import IProducerService
from schemas import ProducerCreate, ProducerRead, ProducerUpdate


class ProducerService(IProducerService):
    """Service class for managing producer-related business logic."""

    def __init__(self, producer_repository: IProducerRepository):
        """Initialize the ProducerService with a producer repository."""
        self.producer_repository = producer_repository

    def get_all_producers(self) -> list[ProducerRead]:
        return self.producer_repository.get_all()

    def get_producer_by_id(self, producer_id: int) -> ProducerRead:
        return self.producer_repository.get_by_id(producer_id)

    def create_producer(self, producer_data: ProducerCreate) -> ProducerRead:
        return self.producer_repository.create(producer_data)

    def update_producer(
        self, producer_id: int, producer_data: ProducerUpdate
    ) -> ProducerRead:
        return self.producer_repository.update(producer_id, producer_data)

    def delete_producer(self, producer_id: int) -> bool:
        return self.producer_repository.delete(producer_id)
