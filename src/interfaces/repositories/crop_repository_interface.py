from src.models import Crop

from .base_repository_interface import IBaseRepository


class ICropRepository(IBaseRepository[Crop]):
    """Repository interface for Crop-specific methods."""

    pass
