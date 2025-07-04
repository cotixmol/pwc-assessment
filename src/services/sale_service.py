from dtos import SaleCreate, SaleRead, SaleUpdate
from interfaces.repositories import ISaleRepository
from interfaces.services import ISaleService


class SaleService(ISaleService):
    """Service class for managing sale-related business logic."""

    def __init__(self, sale_repository: ISaleRepository):
        """Initialize the SaleService with a sale repository."""
        self.sale_repository = sale_repository

    def get_all_sales(self) -> list[SaleRead]:
        return self.sale_repository.get_all()

    def get_sale_by_id(self, sale_id: int) -> SaleRead:
        return self.sale_repository.get_by_id(sale_id)

    def create_sale(self, sale_data: SaleCreate) -> SaleRead:
        return self.sale_repository.create(sale_data)

    def update_sale(self, sale_id: int, sale_data: SaleUpdate) -> SaleRead:
        return self.sale_repository.update(sale_id, sale_data)

    def delete_sale(self, sale_id: int) -> bool:
        return self.sale_repository.delete(sale_id)
