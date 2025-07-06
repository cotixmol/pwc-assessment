from src.dtos import SaleCreate, SaleRead, SaleUpdate
from src.exceptions import InsufficientStockError, SaleNotFoundError
from src.interfaces.repositories import ISaleRepository
from src.interfaces.services import ISaleService, IStockService


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
        available_stock_before = await self.stock_service.get_available_stock(
            sale_data.producer_id, sale_data.crop_type
        )
        if sale_data.quantity_sold > available_stock_before:
            raise InsufficientStockError(
                sale_data.quantity_sold, available_stock_before
            )

        created_sale = await self.sale_repository.create(sale_data.model_dump())

        sale_to_return = SaleRead.model_validate(created_sale)

        sale_to_return.available_stock = (
            available_stock_before - created_sale.quantity_sold
        )

        return sale_to_return

    async def update_sale(self, sale_id: int, sale_data: SaleUpdate) -> SaleRead:
        """Updates a sale and returns its data including the remaining available stock."""
        existing_sale = await self.sale_repository.get_by_id(sale_id)
        if not existing_sale:
            raise SaleNotFoundError(sale_id)

        new_quantity_sold = (
            sale_data.quantity_sold
            if sale_data.quantity_sold is not None
            else existing_sale.quantity_sold
        )

        current_available_stock = await self.stock_service.get_available_stock(
            existing_sale.producer_id, existing_sale.crop_type
        )
        effective_stock = current_available_stock + existing_sale.quantity_sold

        if new_quantity_sold > effective_stock:
            raise InsufficientStockError(new_quantity_sold, effective_stock)

        updated_sale = await self.sale_repository.update(
            sale_id, sale_data.model_dump(exclude_unset=True)
        )

        sale_to_return = SaleRead.model_validate(updated_sale)

        sale_to_return.available_stock = effective_stock - updated_sale.quantity_sold

        return sale_to_return

    async def delete_sale(self, sale_id: int) -> bool:
        existing_sale = await self.sale_repository.get_by_id(sale_id)
        if not existing_sale:
            raise SaleNotFoundError(sale_id)
        return await self.sale_repository.delete(sale_id)
