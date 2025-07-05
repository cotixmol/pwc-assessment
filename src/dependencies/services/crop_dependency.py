from typing import Annotated

from fastapi import Depends

from src.dependencies.repositories import get_crop_sql_repository
from src.interfaces.repositories import ICropRepository
from src.interfaces.services import ICropService
from src.services import CropService

CropRepo = Annotated[ICropRepository, Depends(get_crop_sql_repository)]


def get_crop_service(crop_repository: CropRepo) -> ICropService:
    """Get the crop service with its repository dependency."""
    return CropService(crop_repository)
