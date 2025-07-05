from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.services import get_harvest_service
from src.dtos.harvest import HarvestCreate, HarvestRead, HarvestUpdate
from src.exceptions import HarvestNotFoundError
from src.interfaces.services import IHarvestService

harvest_router = APIRouter(prefix="/harvests", tags=["Harvests"])


@harvest_router.get("/", response_model=list[HarvestRead])
async def read_harvests(
    service: Annotated[IHarvestService, Depends(get_harvest_service)],
):
    """
    Retrieve all harvests.
    """
    return await service.get_all_harvests()


@harvest_router.get("/{harvest_id}", response_model=HarvestRead)
async def read_harvest(
    harvest_id: int, service: Annotated[IHarvestService, Depends(get_harvest_service)]
):
    """
    Retrieve a harvest by its ID.
    """
    try:
        return await service.get_harvest_by_id(harvest_id)
    except HarvestNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@harvest_router.post(
    "/", response_model=HarvestRead, status_code=status.HTTP_201_CREATED
)
async def create_harvest(
    harvest: HarvestCreate,
    service: Annotated[IHarvestService, Depends(get_harvest_service)],
):
    """
    Create a new harvest.
    """
    return await service.create_harvest(harvest)


@harvest_router.put("/{harvest_id}", response_model=HarvestRead)
async def update_harvest(
    harvest_id: int,
    harvest: HarvestUpdate,
    service: Annotated[IHarvestService, Depends(get_harvest_service)],
):
    """
    Update an existing harvest.
    """
    try:
        return await service.update_harvest(harvest_id, harvest)
    except HarvestNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@harvest_router.delete("/{harvest_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_harvest(
    harvest_id: int, service: Annotated[IHarvestService, Depends(get_harvest_service)]
):
    """
    Delete a harvest by its ID.
    """
    try:
        await service.delete_harvest(harvest_id)
    except HarvestNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
