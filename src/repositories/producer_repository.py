from models import Producer
from repositories import BaseRepository


class ProducerRepository(BaseRepository[Producer]):
    """
    Repository for managing Producer entities in the database."""

    def __init__(self, session):
        super().__init__(Producer, session)
