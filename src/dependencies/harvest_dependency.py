from fastapi import Depends
from config.db import get_db_pool
from repositories import HarvestSQLRepository, BaseSQLRepository
from models import Harvest
from services import HarvestService


def get_harvest_repository(
    session=Depends(get_db_pool),
) -> BaseSQLRepository[Harvest]:
    return HarvestSQLRepository(session)


def get_harvest_service(
    harvest_repository: BaseSQLRepository[Harvest] = Depends(get_harvest_repository),
) -> HarvestService:
    return HarvestService(harvest_repository)
