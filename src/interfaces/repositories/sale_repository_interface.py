from models import Sale

from .base_repository_interface import IBaseRepository


# TODO: Add custom abstract methods for Sale here if needed
class ISaleRepository(IBaseRepository[Sale]):
    """Repository interface for Sale-specific methods."""

    pass
