from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.services import get_sale_service
from src.dtos.sale import SaleCreate, SaleRead, SaleUpdate
from src.exceptions import InsufficientStockError, SaleNotFoundError
from src.interfaces.services import ISaleService

sale_router = APIRouter(prefix="/sales", tags=["Sales"])

SaleService = Annotated[ISaleService, Depends(get_sale_service)]


@sale_router.get("/", response_model=list[SaleRead])
async def read_sales(sale_service: SaleService):
    """
    Retrieve all sales.
    """
    return await sale_service.get_all_sales()


@sale_router.get("/{sale_id}", response_model=SaleRead)
async def read_sale(sale_id: int, sale_service: SaleService):
    """
    Retrieve a sale by its ID.
    """
    try:
        return await sale_service.get_sale_by_id(sale_id)
    except SaleNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@sale_router.post("/", response_model=SaleRead, status_code=status.HTTP_201_CREATED)
async def create_sale(sale: SaleCreate, sale_service: SaleService):
    """
    Create a new sale.
    """
    try:
        return await sale_service.create_sale(sale)
    except InsufficientStockError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e


@sale_router.put("/{sale_id}", response_model=SaleRead)
async def update_sale(
    sale_id: int,
    sale: SaleUpdate,
    sale_service: SaleService,
):
    """
    Update an existing sale.
    """
    try:
        return await sale_service.update_sale(sale_id, sale)
    except SaleNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except InsufficientStockError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e


@sale_router.delete("/{sale_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sale(sale_id: int, sale_service: SaleService):
    """
    Delete a sale by its ID.
    """
    try:
        await sale_service.delete_sale(sale_id)
    except SaleNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
