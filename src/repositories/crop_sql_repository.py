from src.models import Crop
from src.repositories import BaseSQLRepository


class CropSQLRepository(BaseSQLRepository[Crop]):
    """SQL repository for Crop model, providing database operations specific to crops."""

    def __init__(self, session):
        """Use the BaseSQLRepository with the Crop model."""
        super().__init__(Crop, session)
