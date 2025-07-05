from typing import Annotated

from fastapi import Depends

from src.dependencies.repositories import (
    get_harvest_sql_repository,
    get_sale_sql_repository,
)
from src.interfaces.repositories import IHarvestRepository, ISaleRepository
from src.interfaces.services import IStockService
from src.services import StockService

HarvestRepo = Annotated[IHarvestRepository, Depends(get_harvest_sql_repository)]
SaleRepo = Annotated[ISaleRepository, Depends(get_sale_sql_repository)]


def get_stock_service(
    harvest_repository: HarvestRepo, sale_repository: SaleRepo
) -> IStockService:
    """Get the stock service with its repository dependencies."""
    return StockService(
        harvest_repository=harvest_repository, sale_repository=sale_repository
    )
