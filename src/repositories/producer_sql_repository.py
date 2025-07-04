from models import Producer

from repositories import BaseSQLRepository


class ProducerSQLRepository(BaseSQLRepository[Producer]):
    """Repository for managing Producer entities in the database."""

    def __init__(self, session):
        """Use the BaseSQLRepository to handle CRUD operations for Producer."""
        super().__init__(Producer, session)
