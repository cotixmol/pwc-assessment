from models import Sale

from repositories import BaseSQLRepository


class SaleSQLRepository(BaseSQLRepository[Sale]):
    """Repository for managing Sale entities in the database."""

    def __init__(self, session):
        """Uses the BaseSQLRepository to handle CRUD operations for Sale."""
        super().__init__(Sale, session)
