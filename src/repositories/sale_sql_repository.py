from models import Sale

from repositories import BaseSQLRepository


class SaleSQLRepository(BaseSQLRepository[Sale]):
    """SQL repository for Crop model, providing database operations specific to sales."""

    def __init__(self, session):
        """Use the BaseSQLRepository with the Sale model."""
        super().__init__(Sale, session)
