from dtos import SaleCreate, SaleRead, SaleUpdate
from exceptions import InsufficientStockError, SaleNotFoundError
from interfaces.repositories import ISaleRepository
from interfaces.services import ISaleService, IStockService


class SaleService(ISaleService):
    """Service class for managing sale-related business logic."""

    def __init__(self, sale_repository: ISaleRepository, stock_service: IStockService):
        """Initialize the SaleService with a sale repository."""
        self.sale_repository = sale_repository
        self.stock_service = stock_service

    async def get_all_sales(self) -> list[SaleRead]:
        return await self.sale_repository.get_all()

    async def get_sale_by_id(self, sale_id: int) -> SaleRead:
        sale = await self.sale_repository.get_by_id(sale_id)
        if not sale:
            raise SaleNotFoundError(sale_id)
        return sale

    async def create_sale(self, sale_data: SaleCreate) -> SaleRead:
        available_stock = await self.stock_service.get_available_stock(
            sale_data.producer_id, sale_data.crop_type
        )
        if sale_data.quantity_sold > available_stock:
            raise InsufficientStockError(sale_data.quantity_sold, available_stock)
        return await self.sale_repository.create(sale_data.model_dump())

    async def update_sale(self, sale_id: int, sale_data: SaleUpdate) -> SaleRead:
        existing_sale = await self.sale_repository.get_by_id(sale_id)
        if not existing_sale:
            raise SaleNotFoundError(sale_id)
        new_quantity_sold = (
            sale_data.quantity_sold
            if sale_data.quantity_sold is not None
            else existing_sale.quantity_sold
        )
        available_stock = await self.stock_service.get_available_stock(
            existing_sale.producer_id, existing_sale.crop_type
        )
        effective_stock = available_stock + existing_sale.quantity_sold

        if new_quantity_sold > effective_stock:
            raise InsufficientStockError(new_quantity_sold, effective_stock)
        return await self.sale_repository.update(
            sale_id, sale_data.model_dump(exclude_unset=True)
        )

    async def delete_sale(self, sale_id: int) -> bool:
        existing_sale = await self.sale_repository.get_by_id(sale_id)
        if not existing_sale:
            raise SaleNotFoundError(sale_id)
        return await self.sale_repository.delete(sale_id)
