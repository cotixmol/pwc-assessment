from models import Sale

from repositories import BaseSQLRepository


class SaleSQLRepository(BaseSQLRepository[Sale]):
    """
    Repository for managing Sale entities in the database."""

    def __init__(self, session):
        super().__init__(Sale, session)
