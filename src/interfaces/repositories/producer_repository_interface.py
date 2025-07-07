from src.models import Producer

from .base_repository_interface import IBaseRepository


class IProducerRepository(IBaseRepository[Producer]):
    """Repository interface for Producer-specific methods."""

    pass
