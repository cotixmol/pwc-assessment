from typing import Annotated

from asyncpg import Pool
from config.db import get_db_pool
from fastapi import Depends
from models import Producer
from repositories import BaseSQLRepository, ProducerSQLRepository
from services import ProducerService


def get_producer_repository(
    session: Annotated[Pool, Depends(get_db_pool)],
) -> BaseSQLRepository[Producer]:
    """Get the producer repository with its session dependency."""
    return ProducerSQLRepository(session)


def get_producer_service(
    producer_repository: Annotated[
        BaseSQLRepository[Producer], Depends(get_producer_repository)
    ],
) -> ProducerService:
    """Get the producer service with its repository dependency."""
    return ProducerService(producer_repository)
