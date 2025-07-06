from src.exceptions import ProducerNotFoundError
from src.interfaces.repositories import (
    IHarvestRepository,
    IProducerRepository,
    ISaleRepository,
)
from src.interfaces.services import IStockService
from src.models import CropType


class StockService(IStockService):
    """
    Service for handling all business logic related to stock and inventory.
    """

    def __init__(
        self,
        harvest_repository: IHarvestRepository,
        sale_repository: ISaleRepository,
        producer_repository: IProducerRepository,
    ):
        self.harvest_repository = harvest_repository
        self.sale_repository = sale_repository
        self.producer_repository = producer_repository

    async def get_available_stock(self, producer_id: int, crop_type: CropType) -> float:
        producer = await self.producer_repository.get_by_id(producer_id)
        if not producer:
            raise ProducerNotFoundError(producer_id)

        total_harvested = (
            await self.harvest_repository.get_total_harvested_by_producer_and_crop_type(
                producer_id, crop_type
            )
        )
        total_sold = (
            await self.sale_repository.get_total_sold_by_producer_and_crop_type(
                producer_id, crop_type
            )
        )

        return total_harvested - total_sold
