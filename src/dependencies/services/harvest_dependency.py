from typing import Annotated

from fastapi import Depends

from src.dependencies.repositories import get_harvest_sql_repository
from src.interfaces.repositories import IHarvestRepository
from src.interfaces.services import IHarvestService
from src.services import HarvestService

HarvestRepo = Annotated[IHarvestRepository, Depends(get_harvest_sql_repository)]


def get_harvest_service(harvest_repository: HarvestRepo) -> IHarvestService:
    """Get the harvest service with its repository dependency."""
    return HarvestService(harvest_repository)
