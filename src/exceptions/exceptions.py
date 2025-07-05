class InsufficientStockError(Exception):
    """Custom exception for when a sale quantity exceeds harvest stock."""

    def __init__(self, quantity_sold: str, harvest_quantity: str):
        self.message = f"Quantity sold ({quantity_sold}) cannot exceed harvest quantity ({harvest_quantity})."
        super().__init__(self.message)


class HarvestNotFoundError(Exception):
    """Custom exception for when a harvest is not found."""

    def __init__(self, harvest_id: int):
        self.message = f"Harvest with ID {harvest_id} not found."
        super().__init__(self.message)


class SaleNotFoundError(Exception):
    """Custom exception for when a sale is not found."""

    def __init__(self, sale_id: int):
        self.message = f"Sale with ID {sale_id} not found."
        super().__init__(self.message)
