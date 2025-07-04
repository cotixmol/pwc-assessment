from abc import ABC, abstractmethod


class ISaleService(ABC):
    """Interface for Sale Service."""

    @abstractmethod
    def get_all_sales(self):
        """Retrieve all sales."""
        pass

    @abstractmethod
    def get_sale_by_id(self, sale_id):
        """Retrieve a sale by its ID."""
        pass

    @abstractmethod
    def create_sale(self, sale_data):
        """Create a new sale."""
        pass

    @abstractmethod
    def update_sale(self, sale_id, sale_data):
        """Update an existing sale."""
        pass

    @abstractmethod
    def delete_sale(self, sale_id):
        """Delete a sale by its ID."""
        pass
