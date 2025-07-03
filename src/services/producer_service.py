from interfaces.services import IProducerService


class ProducerService(IProducerService):
    def __init__(self, producer_repository):
        self.producer_repository = producer_repository

    def get_all_producers(self):
        return self.producer_repository.get_all()

    def get_producer_by_id(self, id):
        return self.producer_repository.get_by_id(id)

    def create_producer(self, producer_data):
        return self.producer_repository.create(producer_data)

    def update_producer(self, id, producer_data):
        return self.producer_repository.update(id, producer_data)

    def delete_producer(self, id):
        return self.producer_repository.delete(id)
