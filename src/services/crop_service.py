from interfaces.services import ICropService


class CropService(ICropService):
    def __init__(self, crop_repository):
        self.crop_repository = crop_repository

    def get_all_crops(self):
        return self.crop_repository.get_all()

    def get_crop_by_id(self, id):
        return self.crop_repository.get_by_id(id)

    def create_crop(self, crop_data):
        return self.crop_repository.create(crop_data)

    def update_crop(self, id, crop_data):
        return self.crop_repository.update(id, crop_data)

    def delete_crop(self, id):
        return self.crop_repository.delete(id)
