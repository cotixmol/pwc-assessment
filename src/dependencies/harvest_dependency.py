from typing import Annotated

from asyncpg import Pool
from config.db import get_db_pool
from fastapi import Depends
from interfaces.repositories import IHarvestRepository
from interfaces.services import IHarvestService
from repositories import HarvestSQLRepository
from services import HarvestService


def get_harvest_repository(
    session: Annotated[Pool, Depends(get_db_pool)],
) -> IHarvestRepository:
    """Get the harvest repository with its session dependency."""
    return HarvestSQLRepository(session)


def get_harvest_service(
    harvest_repository: Annotated[IHarvestRepository, Depends(get_harvest_repository)],
) -> IHarvestService:
    """Get the harvest service with its repository dependency."""
    return HarvestService(harvest_repository)
