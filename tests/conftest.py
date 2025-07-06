from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app
from src.dependencies.services import get_producer_service
from src.services.producer_service import ProducerService
from tests.fakes.fake_producer_repository import FakeProducerRepository


@pytest.fixture(scope="module")
def test_producer_client():
    """
    TestClient instance for integration tests in the Producer module.
    """
    fake_producer_repo = FakeProducerRepository()
    mock_stock_service = MagicMock()
    mock_stock_service.get_available_stock = AsyncMock()

    def fake_get_producer_service():
        return ProducerService(
            producer_repository=fake_producer_repo, stock_service=mock_stock_service
        )

    app.dependency_overrides[get_producer_service] = fake_get_producer_service

    with TestClient(app) as client:
        yield client, fake_producer_repo, mock_stock_service

    app.dependency_overrides.clear()
