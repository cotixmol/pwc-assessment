from models import Producer
from repositories import BaseSQLRepository


class ProducerSQLRepository(BaseSQLRepository[Producer]):
    """SQL repository for Crop model, providing database operations specific to producers."""

    def __init__(self, session):
        """Use the BaseSQLRepository with the Producer model."""
        super().__init__(Producer, session)
