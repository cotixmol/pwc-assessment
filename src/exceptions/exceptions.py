# src/exceptions.py


class NotFoundError(Exception):
    """Base class for not found errors."""

    def __init__(self, item_id: int, item_name: str):
        self.item_id = item_id
        self.item_name = item_name
        super().__init__(f"{self.item_name} with ID {self.item_id} not found")


class CropNotFoundError(NotFoundError):
    """Raised when a crop is not found."""

    def __init__(self, crop_id: int):
        super().__init__(item_id=crop_id, item_name="Crop")


class HarvestNotFoundError(NotFoundError):
    """Raised when a harvest is not found."""

    def __init__(self, harvest_id: int):
        super().__init__(item_id=harvest_id, item_name="Harvest")


class ProducerNotFoundError(NotFoundError):
    """Raised when a producer is not found."""

    def __init__(self, producer_id: int):
        super().__init__(item_id=producer_id, item_name="Producer")


class SaleNotFoundError(NotFoundError):
    """Raised when a sale is not found."""

    def __init__(self, sale_id: int):
        super().__init__(item_id=sale_id, item_name="Sale")


class InsufficientStockError(Exception):
    """Raised when there is not enough stock to complete a sale."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class RepositoryError(Exception):
    """Raised for general repository-level errors."""

    def __init__(self, message: str = "An error occurred in the repository"):
        self.message = message
        super().__init__(self.message)
