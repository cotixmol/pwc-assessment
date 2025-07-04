from abc import ABC, abstractmethod


class ICropService(ABC):
    """
    Interface for Crop Service.
    """

    @abstractmethod
    def get_all_crops(self):
        pass

    @abstractmethod
    def get_crop_by_id(self, id):
        pass

    @abstractmethod
    def create_crop(self, crop_data):
        pass

    @abstractmethod
    def update_crop(self, id, crop_data):
        pass

    @abstractmethod
    def delete_crop(self, id):
        pass
