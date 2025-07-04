from typing import Annotated

from asyncpg import Pool
from config.db import get_db_pool
from fastapi import Depends
from interfaces.repositories import ICropRepository
from interfaces.services import ICropService
from repositories import CropSQLRepository
from services import CropService


def get_crop_repository(
    session: Annotated[Pool, Depends(get_db_pool)],
) -> ICropRepository:
    """Get the crop repository with its session dependency."""
    return CropSQLRepository(session)


def get_crop_service(
    crop_repository: Annotated[ICropRepository, Depends(get_crop_repository)],
) -> ICropService:
    """Get the crop service with its repository dependency."""
    return CropService(crop_repository)
