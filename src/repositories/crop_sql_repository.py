from models import Crop

from repositories import BaseSQLRepository


class CropSQLRepository(BaseSQLRepository[Crop]):
    """
    Repository for managing Crop entities in the database."""

    def __init__(self, session):
        super().__init__(Crop, session)
