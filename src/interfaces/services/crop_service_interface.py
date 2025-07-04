from abc import ABC, abstractmethod


class ICropService(ABC):
    """Interface for Crop Service."""

    @abstractmethod
    def get_all_crops(self):
        """Retrieve all crops."""
        pass

    @abstractmethod
    def get_crop_by_id(self, crop_id):
        """Retrieve a crop by its ID."""
        pass

    @abstractmethod
    def create_crop(self, crop_data):
        """Create a new crop."""
        pass

    @abstractmethod
    def update_crop(self, crop_id, crop_data):
        """Update an existing crop."""
        pass

    @abstractmethod
    def delete_crop(self, crop_id):
        """Delete a crop by its ID."""
        pass
