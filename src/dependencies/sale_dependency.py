from typing import Annotated

from asyncpg import Pool
from config.db import get_db_pool
from fastapi import Depends
from models import Sale
from repositories import BaseSQLRepository, SaleSQLRepository
from services import SaleService


def get_sale_repository(
    session: Annotated[Pool, Depends(get_db_pool)],
) -> BaseSQLRepository[Sale]:
    return SaleSQLRepository(session)


def get_sale_service(
    sale_repository: Annotated[BaseSQLRepository[Sale], Depends(get_sale_repository)],
) -> SaleService:
    return SaleService(sale_repository)
