from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.services import get_producer_service
from src.dtos.producer import ProducerCreate, ProducerRead, ProducerUpdate
from src.exceptions import DeletionError, ProducerNotFoundError
from src.interfaces.services import IProducerService

producer_router = APIRouter(prefix="/producers", tags=["Producers"])

ProducerService = Annotated[IProducerService, Depends(get_producer_service)]


@producer_router.get("/", response_model=list[ProducerRead])
async def read_producers(
    producer_service: ProducerService,
):
    """
    Retrieve all producers.
    """
    return await producer_service.get_all_producers()


@producer_router.get("/{producer_id}", response_model=ProducerRead)
async def read_producer(
    producer_id: int,
    producer_service: ProducerService,
):
    """
    Retrieve a producer by its ID.
    """
    try:
        return await producer_service.get_producer_by_id(producer_id)
    except ProducerNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@producer_router.post(
    "/", response_model=ProducerRead, status_code=status.HTTP_201_CREATED
)
async def create_producer(
    producer: ProducerCreate,
    producer_service: ProducerService,
):
    """
    Create a new producer.
    """
    return await producer_service.create_producer(producer)


@producer_router.put("/{producer_id}", response_model=ProducerRead)
async def update_producer(
    producer_id: int,
    producer: ProducerUpdate,
    producer_service: ProducerService,
):
    """
    Update an existing producer.
    """
    try:
        return await producer_service.update_producer(producer_id, producer)
    except ProducerNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@producer_router.delete("/{producer_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_producer(
    producer_id: int,
    producer_service: ProducerService,
):
    """
    Delete a producer by its ID.
    """
    try:
        await producer_service.delete_producer(producer_id)
        return {"detail": f"Producer ID: {producer_id} deleted successfully"}
    except ProducerNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except DeletionError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e
