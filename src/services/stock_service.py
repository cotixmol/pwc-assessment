from interfaces.repositories import IHarvestRepository, ISaleRepository
from interfaces.services import IStockService
from models.crop import CropType


class StockService(IStockService):
    """
    Service for handling all business logic related to stock and inventory.
    """

    def __init__(
        self, harvest_repository: IHarvestRepository, sale_repository: ISaleRepository
    ):
        self.harvest_repository = harvest_repository
        self.sale_repository = sale_repository

    async def get_available_stock(self, producer_id: int, crop_type: CropType) -> float:
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
