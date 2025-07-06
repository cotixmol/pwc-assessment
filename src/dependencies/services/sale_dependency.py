from typing import Annotated

from fastapi import Depends

from src.dependencies.repositories import get_sale_sql_repository
from src.dependencies.services.stock_dependency import get_stock_service
from src.interfaces.repositories import ISaleRepository
from src.interfaces.services import ISaleService, IStockService
from src.services import SaleService

SaleRepo = Annotated[ISaleRepository, Depends(get_sale_sql_repository)]
StockService = Annotated[IStockService, Depends(get_stock_service)]


def get_sale_service(
    sale_repository: SaleRepo, stock_service: StockService
) -> ISaleService:
    """Get the sale service with its repository and stock service dependencies."""
    return SaleService(sale_repository=sale_repository, stock_service=stock_service)
