from fastapi import Depends
from src.config.db import get_db_pool
from src.repositories.producer_repository import ProducerRepository
from services import ProducerService


def get_producer_repository(
    session = Depends(get_db_pool),
) -> ProducerRepository:
    return ProducerRepository(session)


def get_producer_service(
    producer_repository: ProducerRepository = Depends(get_producer_repository),
) -> ProducerService:
    return ProducerService(producer_repository)
