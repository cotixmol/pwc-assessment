from models import Harvest
from repositories import BaseRepository


class HarvestRepository(BaseRepository[Harvest]):
    """
    Repository for managing Harvest entities in the database."""

    def __init__(self, session):
        super().__init__(Harvest, session)
