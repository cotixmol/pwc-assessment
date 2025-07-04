from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from models import Base

T = TypeVar("T", bound=Base)  # type: ignore


class IBaseRepository(ABC, Generic[T]):
    """It defines the common methods to implement in the base repository."""

    @abstractmethod
    async def get_all(self) -> List[T]:
        """Get all objects of this type."""
        pass

    @abstractmethod
    async def get_by_id(self, obj_id: int) -> T | None:
        """Get an object of this type by its primary key."""
        pass

    @abstractmethod
    async def create(self, data: dict) -> T:
        """Create a new object of this type."""
        pass

    @abstractmethod
    async def update(self, obj_id: int, data: dict) -> T | None:
        """Update an existing object of this type."""
        pass

    @abstractmethod
    async def delete(self, obj_id: int) -> bool:
        """Delete an object of this type by its ID."""
        pass
