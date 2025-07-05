from abc import ABC, abstractmethod

from dtos import SaleCreate, SaleRead, SaleUpdate


class ISaleService(ABC):
    """Interface for Sale Service."""

    @abstractmethod
    def get_all_sales(self) -> list[SaleRead]:
        """Retrieve all sales."""
        pass

    @abstractmethod
    def get_sale_by_id(self, sale_id: int) -> SaleRead:
        """Retrieve a sale by its ID."""
        pass

    @abstractmethod
    def create_sale(self, sale_data: SaleCreate) -> SaleRead:
        """Creates a new sale after validating the available stock for the crop type."""
        pass

    @abstractmethod
    def update_sale(self, sale_id: int, sale_data: SaleUpdate) -> SaleRead:
        """Updates an existing sale, re-validating stock levels."""
        pass

    @abstractmethod
    def delete_sale(self, sale_id: int) -> bool:
        """Delete a sale by its ID."""
        pass
