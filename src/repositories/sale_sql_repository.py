from interfaces.repositories import ISaleRepository
from models import CropType, Sale
from repositories import BaseSQLRepository
from sqlalchemy import func


class SaleSQLRepository(BaseSQLRepository[Sale], ISaleRepository):
    """SQL repository for Crop model, providing database operations specific to sales."""

    def __init__(self, session):
        """Use the BaseSQLRepository with the Sale model."""
        super().__init__(Sale, session)

    def get_total_sold_by_producer_and_crop_type(
        self, producer_id: int, crop_type: CropType
    ) -> float:
        total_sold = (
            self.session.query(func.sum(Sale.quantity_sold))
            .filter(Sale.producer_id == producer_id, Sale.crop_type == crop_type)
            .scalar()
        )
        return total_sold or 0.0
