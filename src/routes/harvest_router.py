from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.services import get_harvest_service
from src.dtos.harvest import HarvestCreate, HarvestRead, HarvestUpdate
from src.exceptions import (
    CropNotFoundError,
    HarvestNotFoundError,
    ProducerNotFoundError,
)
from src.interfaces.services import IHarvestService

harvest_router = APIRouter(prefix="/harvests", tags=["Harvests"])

HarvestService = Annotated[IHarvestService, Depends(get_harvest_service)]


@harvest_router.get("/", response_model=list[HarvestRead])
async def read_harvests(
    harvest_service: HarvestService,
):
    """
    Retrieve all harvests.
    """
    return await harvest_service.get_all_harvests()


@harvest_router.get("/{harvest_id}", response_model=HarvestRead)
async def read_harvest(harvest_id: int, harvest_service: HarvestService):
    """
    Retrieve a harvest by its ID.
    """
    try:
        return await harvest_service.get_harvest_by_id(harvest_id)
    except HarvestNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@harvest_router.post(
    "/", response_model=HarvestRead, status_code=status.HTTP_201_CREATED
)
async def create_harvest(
    harvest: HarvestCreate,
    harvest_service: HarvestService,
):
    """
    Create a new harvest.
    """
    try:
        return await harvest_service.create_harvest(harvest)
    except (HarvestNotFoundError, CropNotFoundError, ProducerNotFoundError) as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@harvest_router.put("/{harvest_id}", response_model=HarvestRead)
async def update_harvest(
    harvest_id: int,
    harvest: HarvestUpdate,
    harvest_service: HarvestService,
):
    """
    Update an existing harvest.
    """
    try:
        return await harvest_service.update_harvest(harvest_id, harvest)
    except HarvestNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@harvest_router.delete("/{harvest_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_harvest(harvest_id: int, harvest_service: HarvestService):
    """
    Delete a harvest by its ID.
    """
    try:
        await harvest_service.delete_harvest(harvest_id)
        return {"detail": f"Harvest ID: {harvest_id} deleted successfully"}
    except HarvestNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
