from typing import Annotated

from asyncpg import Pool
from config.db import get_db_pool
from fastapi import Depends
from models import Crop
from repositories import BaseSQLRepository, CropSQLRepository
from services import CropService


def get_crop_repository(
    session: Annotated[Pool, Depends(get_db_pool)],
) -> BaseSQLRepository[Crop]:
    return CropSQLRepository(session)


def get_crop_service(
    crop_repository: Annotated[BaseSQLRepository[Crop], Depends(get_crop_repository)],
) -> CropService:
    return CropService(crop_repository)
