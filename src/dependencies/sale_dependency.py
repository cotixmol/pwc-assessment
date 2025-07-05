from typing import Annotated

from asyncpg import Pool
from config.db import get_db_pool
from dependencies import get_stock_service
from fastapi import Depends
from interfaces.repositories import ISaleRepository
from interfaces.services import ISaleService, IStockService
from repositories import SaleSQLRepository
from services import SaleService


def get_sale_repository(
    session: Annotated[Pool, Depends(get_db_pool)],
) -> ISaleRepository:
    """Get the sale repository with its session dependency."""
    return SaleSQLRepository(session)


def get_sale_service(
    sale_repository: Annotated[ISaleRepository, Depends(get_sale_repository)],
    stock_service: Annotated[IStockService, Depends(get_stock_service)],
) -> ISaleService:
    """Get the sale service with its repository dependency."""
    return SaleService(sale_repository)
