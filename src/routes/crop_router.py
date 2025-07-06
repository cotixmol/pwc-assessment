from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.services import get_crop_service
from src.dtos.crop import CropCreate, CropRead, CropUpdate
from src.exceptions import CropNotFoundError
from src.interfaces.services import ICropService

crop_router = APIRouter(prefix="/crops", tags=["Crops"])

CropService = Annotated[ICropService, Depends(get_crop_service)]


@crop_router.get("/", response_model=list[CropRead])
async def read_crops(crop_service: CropService):
    """
    Retrieve all crops.
    """
    return await crop_service.get_all_crops()


@crop_router.get("/{crop_id}", response_model=CropRead)
async def read_crop(crop_id: int, crop_service: CropService):
    """
    Retrieve a crop by its ID.
    """
    try:
        return await crop_service.get_crop_by_id(crop_id)
    except CropNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@crop_router.post("/", response_model=CropRead, status_code=status.HTTP_201_CREATED)
async def create_crop(crop: CropCreate, crop_service: CropService):
    """
    Create a new crop.
    """
    return await crop_service.create_crop(crop)


@crop_router.put("/{crop_id}", response_model=CropRead)
async def update_crop(
    crop_id: int,
    crop: CropUpdate,
    crop_service: CropService,
):
    """
    Update an existing crop.
    """
    try:
        return await crop_service.update_crop(crop_id, crop)
    except CropNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@crop_router.delete("/{crop_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_crop(crop_id: int, crop_service: CropService):
    """
    Delete a crop by its ID.
    """
    try:
        await crop_service.delete_crop(crop_id)
        return {"detail": f"Crop ID: {crop_id} deleted successfully"}
    except CropNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
