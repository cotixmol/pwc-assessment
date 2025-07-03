from models import Sale
from repositories import BaseRepository


class SaleRepository(BaseRepository[Sale]):
    """
    Repository for managing Sale entities in the database."""

    def __init__(self, session):
        super().__init__(Sale, session)
