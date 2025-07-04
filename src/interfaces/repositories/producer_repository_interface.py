from models import Producer

from .base_repository_interface import IBaseRepository


# TODO: Add custom abstract methods for Producer here if needed
class IProducerRepository(IBaseRepository[Producer]):
    """Repository interface for Producer-specific methods."""

    pass
