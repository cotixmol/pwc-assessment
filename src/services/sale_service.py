from interfaces.services import ISaleService


class SaleService(ISaleService):
    """Service class for managing sale-related operations."""

    def __init__(self, sale_repository):
        """Initialize the SaleService with a sale repository."""
        self.sale_repository = sale_repository

    def get_all_sales(self):
        return self.sale_repository.get_all()

    def get_sale_by_id(self, sale_id):
        return self.sale_repository.get_by_id(sale_id)

    def create_sale(self, sale_data):
        return self.sale_repository.create(sale_data)

    def update_sale(self, sale_id, sale_data):
        return self.sale_repository.update(sale_id, sale_data)

    def delete_sale(self, sale_id):
        return self.sale_repository.delete(sale_id)
