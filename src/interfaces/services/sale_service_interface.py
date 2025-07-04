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
        """Create a new sale."""
        pass

    @abstractmethod
    def update_sale(self, sale_id: int, sale_data: SaleUpdate) -> SaleRead:
        """Update an existing sale."""
        pass

    @abstractmethod
    def delete_sale(self, sale_id: int) -> bool:
        """Delete a sale by its ID."""
        pass
