from models import Crop
from repositories import BaseRepository


class CropRepository(BaseRepository[Crop]):
    """
    Repository for managing Crop entities in the database."""

    def __init__(self, session):
        super().__init__(Crop, session)
