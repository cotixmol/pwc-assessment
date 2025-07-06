from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.db import get_db_session
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

DBSession = Annotated[AsyncSession, Depends(get_db_session)]


def get_crop_sql_repository(session: DBSession) -> ICropRepository:
    """Provides the CropSQLRepository."""
    return CropSQLRepository(session)


def get_harvest_sql_repository(session: DBSession) -> IHarvestRepository:
    """Provides the HarvestSQLRepository."""
    return HarvestSQLRepository(session)


def get_producer_sql_repository(session: DBSession) -> IProducerRepository:
    """Provides the ProducerSQLRepository."""
    return ProducerSQLRepository(session)


def get_sale_sql_repository(session: DBSession) -> ISaleRepository:
    """Provides the SaleSQLRepository."""
    return SaleSQLRepository(session)
