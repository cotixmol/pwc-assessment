from typing import List, Type

from interfaces.repositories import IBaseRepository, T
from sqlalchemy.future import select


class BaseSQLRepository(IBaseRepository[T]):
    """
    Base repository class for common database operations.
    """

    def __init__(self, model: Type[T], session):
        """
        Initializes the repository with a model and a database session.
        """
        self.model = model
        self.session = session

    async def get_all(self) -> List[T]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def get_by_id(self, obj_id: int) -> T | None:
        return await self.session.get(self.model, obj_id)

    async def create(self, obj_data: dict) -> T:
        new_obj = self.model(**obj_data)
        self.session.add(new_obj)
        await self.session.commit()
        await self.session.refresh(new_obj)
        return new_obj

    async def update(self, obj_id: int, data: dict) -> T | None:
        obj = await self.get_by_id(obj_id)
        if obj:
            update_data = {k: v for k, v in data.items() if v is not None}
            for key, value in update_data.items():
                setattr(obj, key, value)
            await self.session.commit()
            await self.session.refresh(obj)
        return obj

    async def delete(self, obj_id: int) -> bool:
        obj = await self.get_by_id(obj_id)
        if obj:
            await self.session.delete(obj)
            await self.session.commit()
            return True
        return False
