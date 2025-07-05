from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.services import get_crop_service
from src.dtos.crop import CropCreate, CropRead, CropUpdate
from src.exceptions import CropNotFoundError
from src.interfaces.services import ICropService

crop_router = APIRouter(prefix="/crops", tags=["Crops"])


@crop_router.get("/", response_model=list[CropRead])
async def read_crops(service: Annotated[ICropService, Depends(get_crop_service)]):
    """
    Retrieve all crops.
    """
    return await service.get_all_crops()


@crop_router.get("/{crop_id}", response_model=CropRead)
async def read_crop(
    crop_id: int, service: Annotated[ICropService, Depends(get_crop_service)]
):
    """
    Retrieve a crop by its ID.
    """
    try:
        return await service.get_crop_by_id(crop_id)
    except CropNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@crop_router.post("/", response_model=CropRead, status_code=status.HTTP_201_CREATED)
async def create_crop(
    crop: CropCreate, service: Annotated[ICropService, Depends(get_crop_service)]
):
    """
    Create a new crop.
    """
    return await service.create_crop(crop)


@crop_router.put("/{crop_id}", response_model=CropRead)
async def update_crop(
    crop_id: int,
    crop: CropUpdate,
    service: Annotated[ICropService, Depends(get_crop_service)],
):
    """
    Update an existing crop.
    """
    try:
        return await service.update_crop(crop_id, crop)
    except CropNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@crop_router.delete("/{crop_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_crop(
    crop_id: int, service: Annotated[ICropService, Depends(get_crop_service)]
):
    """
    Delete a crop by its ID.
    """
    try:
        await service.delete_crop(crop_id)
    except CropNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
