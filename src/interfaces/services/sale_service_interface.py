from abc import ABC, abstractmethod


class ISaleService(ABC):
    """
    Interface for Sale Service.
    """

    @abstractmethod
    def get_all_sales(self):
        pass

    @abstractmethod
    def get_sale_by_id(self, id):
        pass

    @abstractmethod
    def create_sale(self, sale_data):
        pass

    @abstractmethod
    def update_sale(self, id, sale_data):
        pass

    @abstractmethod
    def delete_sale(self, id):
        pass
