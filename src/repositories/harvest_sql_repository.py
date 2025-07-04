from models import Harvest

from repositories import BaseSQLRepository


class HarvestSQLRepository(BaseSQLRepository[Harvest]):
    """SQL repository for Crop model, providing database operations specific to harvests."""

    def __init__(self, session):
        """Use the BaseSQLRepository with the Harvest model."""
        super().__init__(Harvest, session)
