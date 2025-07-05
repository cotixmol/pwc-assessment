from typing import Annotated

from dependencies.harvest_dependency import get_harvest_repository
from dependencies.sale_dependency import get_sale_repository
from fastapi import Depends
from interfaces.services import IHarvestService, ISaleService, IStockService
from services import StockService


def get_stock_service(
    harvest_repository: Annotated[IHarvestService, Depends(get_harvest_repository)],
    sale_repository: Annotated[ISaleService, Depends(get_sale_repository)],
) -> IStockService:
    """Get the stock service with its repository dependency."""
    return StockService(harvest_repository, sale_repository)
