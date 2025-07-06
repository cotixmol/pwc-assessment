import logging

from sqlalchemy import func, select
from sqlalchemy.exc import SQLAlchemyError

from src.exceptions import RepositoryError
from src.interfaces.repositories import IHarvestRepository
from src.models import Harvest
from src.models.crop import Crop, CropType
from src.repositories import BaseSQLRepository

logger = logging.getLogger(__name__)


class HarvestSQLRepository(BaseSQLRepository[Harvest], IHarvestRepository):
    """SQL repository for Harvest model."""

    def __init__(self, session):
        super().__init__(Harvest, session)

    async def get_total_harvested_by_producer_and_crop_type(
        self, producer_id: int, crop_type: CropType
    ) -> float:
        try:
            stmt = (
                select(func.sum(Harvest.quantity_tonnes))
                .join(Crop, Harvest.crop_id == Crop.id)
                .filter(Harvest.producer_id == producer_id, Crop.type == crop_type)
            )

            result = await self.session.execute(stmt)
            total_harvested = result.scalar()

            return total_harvested or 0.0
        except SQLAlchemyError as e:
            logger.error("Database error in get_total_harvested: %s", e, exc_info=True)
            raise RepositoryError("Failed to retrieve total harvested quantity.") from e
