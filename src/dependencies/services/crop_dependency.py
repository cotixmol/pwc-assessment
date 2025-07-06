from typing import Annotated

from fastapi import Depends

from src.dependencies.repositories import (
    get_crop_sql_repository,
    get_harvest_sql_repository,
    get_sale_sql_repository,
)
from src.interfaces.repositories import (
    ICropRepository,
    IHarvestRepository,
    ISaleRepository,
)
from src.interfaces.services import ICropService
from src.services import CropService

CropRepo = Annotated[ICropRepository, Depends(get_crop_sql_repository)]
HarvestRepo = Annotated[IHarvestRepository, Depends(get_harvest_sql_repository)]
SaleRepo = Annotated[ISaleRepository, Depends(get_sale_sql_repository)]


def get_crop_service(
    crop_repository: CropRepo,
    harvest_repository: HarvestRepo,
    sale_repository: SaleRepo,
) -> ICropService:
    """Get the crop service with its repository dependency."""
    return CropService(
        crop_repository=crop_repository,
        harvest_repository=harvest_repository,
        sale_repository=sale_repository,
    )
