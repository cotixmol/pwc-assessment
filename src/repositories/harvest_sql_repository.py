from models import Harvest

from repositories import BaseSQLRepository


class HarvestSQLRepository(BaseSQLRepository[Harvest]):
    """Repository for managing Harvest entities in the database."""

    def __init__(self, session):
        """Use the BaseSQLRepository to handle CRUD operations for Harvest."""
        super().__init__(Harvest, session)
