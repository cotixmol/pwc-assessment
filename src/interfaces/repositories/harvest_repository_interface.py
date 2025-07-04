from models import Harvest

from .base_repository_interface import IBaseRepository


# TODO: Add custom abstract methods for Harvest here if needed
class IHarvestRepository(IBaseRepository[Harvest]):
    """Repository interface for Harvest-specific methods."""

    pass
