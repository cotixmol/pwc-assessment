from models import Crop

from .base_repository_interface import IBaseRepository


# TODO: Add custom abstract methods for Crop here if needed
class ICropRepository(IBaseRepository[Crop]):
    """Repository interface for Crop-specific methods."""

    pass
