from fastapi import Depends
from config.db import get_db_pool
from repositories import CropSQLRepository, BaseSQLRepository
from models import Crop
from services import CropService


def get_crop_repository(
    session=Depends(get_db_pool),
) -> BaseSQLRepository[Crop]:
    return CropSQLRepository(session)


def get_crop_service(
    crop_repository: BaseSQLRepository[Crop] = Depends(get_crop_repository),
) -> CropService:
    return CropService(crop_repository)
