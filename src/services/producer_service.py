from src.dtos import ProducerCreate, ProducerRead, ProducerUpdate
from src.exceptions import DeletionError, ProducerNotFoundError
from src.interfaces.repositories import IProducerRepository
from src.interfaces.services import IProducerService, IStockService
from src.models.crop import CropType


class ProducerService(IProducerService):
    """Service class for managing producer-related business logic."""

    def __init__(
        self,
        producer_repository: IProducerRepository,
        stock_service: IStockService,
    ):
        """Initialize the ProducerService with its dependencies."""
        self.producer_repository = producer_repository
        self.stock_service = stock_service

    async def get_all_producers(self) -> list[ProducerRead]:
        return await self.producer_repository.get_all()

    async def get_producer_by_id(self, producer_id: int) -> ProducerRead:
        producer = await self.producer_repository.get_by_id(producer_id)
        if not producer:
            raise ProducerNotFoundError(producer_id)
        return producer

    async def create_producer(self, producer_data: ProducerCreate) -> ProducerRead:
        return await self.producer_repository.create(producer_data.model_dump())

    async def update_producer(
        self, producer_id: int, producer_data: ProducerUpdate
    ) -> ProducerRead:
        updated_producer = await self.producer_repository.update(
            producer_id, producer_data.model_dump(exclude_unset=True)
        )
        if not updated_producer:
            raise ProducerNotFoundError(producer_id)
        return updated_producer

    async def delete_producer(self, producer_id: int) -> bool:
        producer = await self.producer_repository.get_by_id(producer_id)
        if not producer:
            raise ProducerNotFoundError(producer_id)

        stock_errors = []
        for crop_type in CropType:
            stock = await self.stock_service.get_available_stock(producer_id, crop_type)
            if stock > 0:
                stock_errors.append(f"{stock} tonnes of {crop_type.value}")

        if stock_errors:
            error_details = ", ".join(stock_errors)
            raise DeletionError(
                f"Producer ID: {producer_id} cannot be deleted. Stock found: {error_details}."
            )

        deleted = await self.producer_repository.delete(producer_id)
        if not deleted:
            raise ProducerNotFoundError(producer_id)
        return deleted
