import enum
from typing import List, Optional

from src.interfaces.repositories import IProducerRepository
from src.models import Producer


class FakeProducerRepository(IProducerRepository):
    """Fake repository for in-memory testing of Producer-related operations."""

    def __init__(self):
        self.producers = []
        self._next_id = 1

    async def get_all(self) -> List[Producer]:
        return self.producers

    async def get_by_id(self, obj_id: int) -> Optional[Producer]:
        for producer in self.producers:
            if producer.id == obj_id:
                return producer
        return None

    async def create(self, data: dict) -> Producer:
        sanitized_data = {
            key: value.value if isinstance(value, enum.Enum) else value
            for key, value in data.items()
        }
        producer = Producer(id=self._next_id, **sanitized_data)
        self.producers.append(producer)
        self._next_id += 1
        return producer

    async def update(self, obj_id: int, data: dict) -> Optional[Producer]:
        for producer in self.producers:
            if producer.id == obj_id:
                for key, value in data.items():
                    setattr(producer, key, value)
                return producer
        return None

    async def delete(self, obj_id: int) -> bool:
        producer_to_delete = None
        for producer in self.producers:
            if producer.id == obj_id:
                producer_to_delete = producer
                break
        if producer_to_delete:
            self.producers.remove(producer_to_delete)
            return True
        return False
