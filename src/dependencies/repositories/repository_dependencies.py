# This new file is our "base layer" of dependencies.
# It only knows about the database and repositories.

from typing import Annotated

from asyncpg import Pool
from fastapi import Depends

from src.config.db import get_db_pool
from src.interfaces.repositories import (
    ICropRepository,
    IHarvestRepository,
    IProducerRepository,
    ISaleRepository,
)
from src.repositories import (
    CropSQLRepository,
    HarvestSQLRepository,
    ProducerSQLRepository,
    SaleSQLRepository,
)

# A single, clean source for the database connection pool
DbPool = Annotated[Pool, Depends(get_db_pool)]


def get_crop_sql_repository(session: DbPool) -> ICropRepository:
    """Provides the CropSQLRepository."""
    return CropSQLRepository(session)


def get_harvest_sql_repository(session: DbPool) -> IHarvestRepository:
    """Provides the HarvestSQLRepository."""
    return HarvestSQLRepository(session)


def get_producer_sql_repository(session: DbPool) -> IProducerRepository:
    """Provides the ProducerSQLRepository."""
    return ProducerSQLRepository(session)


def get_sale_sql_repository(session: DbPool) -> ISaleRepository:
    """Provides the SaleSQLRepository."""
    return SaleSQLRepository(session)
