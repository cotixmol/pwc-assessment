import logging
from typing import List, Type

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select

from src.exceptions import RepositoryError
from src.interfaces.repositories import IBaseRepository, T

logger = logging.getLogger(__name__)


class BaseSQLRepository(IBaseRepository[T]):
    """Base repository class for common database operations using SQLAlchemy."""

    def __init__(self, model: Type[T], session):
        """Initialize the repository with an ORM model and a db session."""
        self.model = model
        self.session = session

    async def get_all(self) -> List[T]:
        try:
            result = await self.session.execute(select(self.model))
            return result.scalars().all()
        except SQLAlchemyError as e:
            logger.error(
                "Database error occurred while getting all objects: %s",
                e,
                exc_info=True,
            )
            raise RepositoryError(
                "Failed to retrieve all objects from the database."
            ) from e

    async def get_by_id(self, obj_id: int) -> T | None:
        try:
            return await self.session.get(self.model, obj_id)
        except SQLAlchemyError as e:
            logger.error(
                "Database error occurred while getting object by ID %d: %s",
                obj_id,
                e,
                exc_info=True,
            )
            raise RepositoryError(f"Failed to retrieve object with ID {obj_id}.") from e

    async def create(self, obj_data: dict) -> T:
        try:
            new_obj = self.model(**obj_data)
            self.session.add(new_obj)
            await self.session.commit()
            await self.session.refresh(new_obj)
            return new_obj
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(
                "Database error occurred during object creation: %s", e, exc_info=True
            )
            raise RepositoryError("Failed to create the object in the database.") from e

    async def update(self, obj_id: int, data: dict) -> T | None:
        try:
            obj = await self.get_by_id(obj_id)
            if obj:
                update_data = data.model_dump(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(obj, key, value)
                await self.session.commit()
                await self.session.refresh(obj)
            return obj
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(
                "Database error occurred while updating object with ID %d: %s",
                obj_id,
                e,
                exc_info=True,
            )
            raise RepositoryError(f"Failed to update object with ID {obj_id}.") from e

    async def delete(self, obj_id: int) -> bool:
        try:
            obj = await self.get_by_id(obj_id)
            if obj:
                await self.session.delete(obj)
                await self.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(
                "Database error occurred while deleting object with ID %d: %s",
                obj_id,
                e,
                exc_info=True,
            )
            raise RepositoryError(f"Failed to delete object with ID {obj_id}.") from e
