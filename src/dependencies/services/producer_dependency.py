from typing import Annotated

from fastapi import Depends

from src.dependencies.repositories import get_producer_sql_repository
from src.interfaces.repositories import IProducerRepository
from src.interfaces.services import IProducerService
from src.services import ProducerService

ProducerRepo = Annotated[IProducerRepository, Depends(get_producer_sql_repository)]


def get_producer_service(producer_repository: ProducerRepo) -> IProducerService:
    """Get the producer service with its repository dependency."""
    return ProducerService(producer_repository)
