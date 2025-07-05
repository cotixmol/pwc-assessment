from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.services import get_producer_service
from src.dtos.producer import ProducerCreate, ProducerRead, ProducerUpdate
from src.exceptions import ProducerNotFoundError
from src.interfaces.services import IProducerService

producer_router = APIRouter(prefix="/producers", tags=["Producers"])


@producer_router.get("/", response_model=list[ProducerRead])
async def read_producers(
    service: Annotated[IProducerService, Depends(get_producer_service)],
):
    """
    Retrieve all producers.
    """
    return await service.get_all_producers()


@producer_router.get("/{producer_id}", response_model=ProducerRead)
async def read_producer(
    producer_id: int,
    service: Annotated[IProducerService, Depends(get_producer_service)],
):
    """
    Retrieve a producer by its ID.
    """
    try:
        return await service.get_producer_by_id(producer_id)
    except ProducerNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@producer_router.post(
    "/", response_model=ProducerRead, status_code=status.HTTP_201_CREATED
)
async def create_producer(
    producer: ProducerCreate,
    service: Annotated[IProducerService, Depends(get_producer_service)],
):
    """
    Create a new producer.
    """
    return await service.create_producer(producer)


@producer_router.put("/{producer_id}", response_model=ProducerRead)
async def update_producer(
    producer_id: int,
    producer: ProducerUpdate,
    service: Annotated[IProducerService, Depends(get_producer_service)],
):
    """
    Update an existing producer.
    """
    try:
        return await service.update_producer(producer_id, producer)
    except ProducerNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@producer_router.delete("/{producer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_producer(
    producer_id: int,
    service: Annotated[IProducerService, Depends(get_producer_service)],
):
    """
    Delete a producer by its ID.
    """
    try:
        await service.delete_producer(producer_id)
    except ProducerNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
