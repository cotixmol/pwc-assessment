from interfaces.repositories import IHarvestRepository
from models import Harvest
from models.crop import Crop, CropType
from repositories import BaseSQLRepository
from sqlalchemy import func


class HarvestSQLRepository(BaseSQLRepository[Harvest], IHarvestRepository):
    """SQL repository for Crop model, providing database operations specific to harvests."""

    def __init__(self, session):
        """Use the BaseSQLRepository with the Harvest model."""
        super().__init__(Harvest, session)

    def get_total_harvested_by_producer_and_crop_type(
        self, producer_id: int, crop_type: CropType
    ) -> float:
        total_harvested = (
            self.session.query(func.sum(Harvest.quantity_tonnes))
            .join(Crop, Harvest.crop_id == Crop.id)
            .filter(Harvest.producer_id == producer_id, Crop.type == crop_type)
            .scalar()
        )
        return total_harvested or 0.0
