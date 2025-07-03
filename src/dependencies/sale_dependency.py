from fastapi import Depends
from config.db import get_db_pool
from repositories import SaleSQLRepository, BaseSQLRepository
from models import Sale
from services import SaleService


def get_sale_repository(
    session=Depends(get_db_pool),
) -> BaseSQLRepository[Sale]:
    return SaleSQLRepository(session)


def get_sale_service(
    sale_repository: BaseSQLRepository[Sale] = Depends(get_sale_repository),
) -> SaleService:
    return SaleService(sale_repository)
