from typing import Annotated

from fastapi import Depends

from src.dependencies.repositories import (
    get_crop_sql_repository,
    get_harvest_sql_repository,
    get_sale_sql_repository,
)
from src.interfaces.repositories import ICropRepository, IHarvestRepository
from src.interfaces.services import IHarvestService
from src.services import HarvestService

HarvestRepo = Annotated[IHarvestRepository, Depends(get_harvest_sql_repository)]
CropRepo = Annotated[ICropRepository, Depends(get_crop_sql_repository)]
SaleRepo = Annotated[IHarvestRepository, Depends(get_sale_sql_repository)]


def get_harvest_service(
    harvest_repository: HarvestRepo,
    crop_repository: CropRepo,
    sale_repository: SaleRepo,
) -> IHarvestService:
    """Get the harvest service with its repository dependency."""
    return HarvestService(
        harvest_repository=harvest_repository,
        crop_repository=crop_repository,
        sale_repository=sale_repository,
    )
