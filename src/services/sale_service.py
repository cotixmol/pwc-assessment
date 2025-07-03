from interfaces.services import ISaleService


class SaleService(ISaleService):
    def __init__(self, sale_repository):
        self.sale_repository = sale_repository

    def get_all_sales(self):
        return self.sale_repository.get_all()

    def get_sale_by_id(self, id):
        return self.sale_repository.get_by_id(id)

    def create_sale(self, sale_data):
        return self.sale_repository.create(sale_data)

    def update_sale(self, id, sale_data):
        return self.sale_repository.update(id, sale_data)

    def delete_sale(self, id):
        return self.sale_repository.delete(id)
