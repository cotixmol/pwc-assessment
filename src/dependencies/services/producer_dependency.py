from typing import Annotated

from fastapi import Depends

from src.dependencies.repositories import (
    get_crop_sql_repository,
    get_producer_sql_repository,
)
from src.dependencies.services.stock_dependency import get_stock_service
from src.interfaces.repositories import ICropRepository, IProducerRepository
from src.interfaces.services import IProducerService, IStockService
from src.services import ProducerService

ProducerRepo = Annotated[IProducerRepository, Depends(get_producer_sql_repository)]
StockService = Annotated[IStockService, Depends(get_stock_service)]
CropRepo = Annotated[ICropRepository, Depends(get_crop_sql_repository)]


def get_producer_service(
    producer_repository: ProducerRepo,
    stock_service: StockService,
    crop_repository: CropRepo,
) -> IProducerService:
    """Get the producer service with its repository dependency."""
    return ProducerService(
        producer_repository=producer_repository,
        stock_service=stock_service,
        crop_repository=crop_repository,
    )
