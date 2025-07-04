from typing import Annotated

from asyncpg import Pool
from config.db import get_db_pool
from fastapi import Depends
from models import Harvest
from repositories import BaseSQLRepository, HarvestSQLRepository
from services import HarvestService


def get_harvest_repository(
    session: Annotated[Pool, Depends(get_db_pool)],
) -> BaseSQLRepository[Harvest]:
    """Get the harvest repository with its session dependency."""
    return HarvestSQLRepository(session)


def get_harvest_service(
    harvest_repository: Annotated[
        BaseSQLRepository[Harvest], Depends(get_harvest_repository)
    ],
) -> HarvestService:
    """Get the harvest service with its repository dependency."""
    return HarvestService(harvest_repository)
