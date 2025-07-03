from fastapi import Depends
from config.db import get_db_pool
from repositories import ProducerSQLRepository, BaseSQLRepository
from models import Producer
from services import ProducerService


def get_producer_repository(
    session=Depends(get_db_pool),
) -> BaseSQLRepository[Producer]:
    return ProducerSQLRepository(session)


def get_producer_service(
    producer_repository: BaseSQLRepository[Producer] = Depends(get_producer_repository),
) -> ProducerService:
    return ProducerService(producer_repository)
