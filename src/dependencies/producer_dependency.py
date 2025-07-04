from typing import Annotated

from asyncpg import Pool
from config.db import get_db_pool
from fastapi import Depends
from interfaces.repositories import IProducerRepository
from interfaces.services import IProducerService
from repositories import ProducerSQLRepository
from services import ProducerService


def get_producer_repository(
    session: Annotated[Pool, Depends(get_db_pool)],
) -> IProducerRepository:
    """Get the producer repository with its session dependency."""
    return ProducerSQLRepository(session)


def get_producer_service(
    producer_repository: Annotated[
        IProducerRepository, Depends(get_producer_repository)
    ],
) -> IProducerService:
    """Get the producer service with its repository dependency."""
    return ProducerService(producer_repository)
