from interfaces.services import ICropService


class CropService(ICropService):
    """Service class for managing crop-related operations."""

    def __init__(self, crop_repository):
        """Initialize the CropService with a crop repository."""
        self.crop_repository = crop_repository

    def get_all_crops(self):
        return self.crop_repository.get_all()

    def get_crop_by_id(self, crop_id):
        return self.crop_repository.get_by_id(crop_id)

    def create_crop(self, crop_data):
        return self.crop_repository.create(crop_data)

    def update_crop(self, crop_id, crop_data):
        return self.crop_repository.update(crop_id, crop_data)

    def delete_crop(self, crop_id):
        return self.crop_repository.delete(crop_id)
