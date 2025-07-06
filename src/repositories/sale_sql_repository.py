import logging

from sqlalchemy import func, select  # Make sure 'select' is imported
from sqlalchemy.exc import SQLAlchemyError

from src.exceptions import RepositoryError
from src.interfaces.repositories import ISaleRepository
from src.models import CropType, Sale
from src.repositories import BaseSQLRepository

logger = logging.getLogger(__name__)


class SaleSQLRepository(BaseSQLRepository[Sale], ISaleRepository):
    """SQL repository for Sale model."""

    def __init__(self, session):
        super().__init__(Sale, session)

    async def get_total_sold_by_producer_and_crop_type(
        self, producer_id: int, crop_type: CropType
    ) -> float:
        try:
            stmt = select(func.sum(Sale.quantity_sold)).filter(
                Sale.producer_id == producer_id, Sale.crop_type == crop_type
            )
            result = await self.session.execute(stmt)
            total_sold = result.scalar()
            return total_sold or 0.0
        except SQLAlchemyError as e:
            logger.error("Database error in get_total_sold: %s", e, exc_info=True)
            raise RepositoryError("Failed to retrieve total sold quantity.") from e
