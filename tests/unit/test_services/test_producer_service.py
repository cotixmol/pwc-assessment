from unittest.mock import AsyncMock, MagicMock

import pytest

from src.dtos.producer import ProducerCreate, ProducerUpdate
from src.exceptions import DeletionError, ProducerNotFoundError
from src.services.producer_service import ProducerService


@pytest.mark.asyncio
async def test_get_all_producers_empty():
    """Test retrieving all producers when none exist."""
    service, mock_producer_repo, _ = create_mocked_producer_service()
    mock_producer_repo.get_all.return_value = []

    result = await service.get_all_producers()

    assert result == []
    mock_producer_repo.get_all.assert_called_once()


def create_mocked_producer_service():
    mock_producer_repo = AsyncMock()
    mock_stock_service = MagicMock()
    mock_stock_service.get_available_stock = AsyncMock()

    service = ProducerService(
        producer_repository=mock_producer_repo,
        stock_service=mock_stock_service,
    )
    return service, mock_producer_repo, mock_stock_service


@pytest.mark.asyncio
async def test_get_all_producers():
    service, mock_producer_repo, _ = create_mocked_producer_service()
    mock_producer_repo.get_all.return_value = [
        {"id": 1, "name": "Test Producer", "email": "test@example.com"}
    ]

    result = await service.get_all_producers()

    assert len(result) == 1
    assert result[0]["name"] == "Test Producer"
    mock_producer_repo.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_producer_by_id_found():
    service, mock_producer_repo, _ = create_mocked_producer_service()
    mock_producer_repo.get_by_id.return_value = {
        "id": 1,
        "name": "Test Producer",
        "email": "test@example.com",
    }

    result = await service.get_producer_by_id(1)

    assert result["id"] == 1
    assert result["name"] == "Test Producer"
    mock_producer_repo.get_by_id.assert_called_once_with(1)


@pytest.mark.asyncio
async def test_get_producer_by_id_not_found():
    service, mock_producer_repo, _ = create_mocked_producer_service()
    mock_producer_repo.get_by_id.return_value = None

    with pytest.raises(ProducerNotFoundError):
        await service.get_producer_by_id(1)
    mock_producer_repo.get_by_id.assert_called_once_with(1)


@pytest.mark.asyncio
async def test_create_producer():
    service, mock_producer_repo, _ = create_mocked_producer_service()
    producer_data = ProducerCreate(name="New Producer", email="new@example.com")
    mock_producer_repo.create.return_value = {"id": 1, **producer_data.model_dump()}

    result = await service.create_producer(producer_data)

    assert result["name"] == "New Producer"
    mock_producer_repo.create.assert_called_once()


@pytest.mark.asyncio
async def test_update_producer_found():
    service, mock_producer_repo, _ = create_mocked_producer_service()
    producer_update = ProducerUpdate(name="Updated Producer")
    mock_producer_repo.update.return_value = {
        "id": 1,
        "name": "Updated Producer",
        "email": "test@example.com",
    }

    result = await service.update_producer(1, producer_update)

    assert result["name"] == "Updated Producer"
    mock_producer_repo.update.assert_called_once()


@pytest.mark.asyncio
async def test_update_producer_not_found():
    service, mock_producer_repo, _ = create_mocked_producer_service()
    producer_update = ProducerUpdate(name="Updated Producer")
    mock_producer_repo.update.return_value = None

    with pytest.raises(ProducerNotFoundError):
        await service.update_producer(1, producer_update)
    mock_producer_repo.update.assert_called_once()


@pytest.mark.asyncio
async def test_delete_producer_with_stock():
    service, mock_producer_repo, mock_stock_service = create_mocked_producer_service()

    mock_stock_service.get_available_stock.return_value = 10.0
    mock_producer_repo.get_by_id.return_value = {
        "id": 1,
        "name": "Test Producer",
        "email": "test@example.com",
    }

    with pytest.raises(DeletionError):
        await service.delete_producer(1)

    mock_producer_repo.get_by_id.assert_called_once_with(1)
    mock_stock_service.get_available_stock.assert_called()


@pytest.mark.asyncio
async def test_delete_producer_no_stock():
    service, mock_producer_repo, mock_stock_service = create_mocked_producer_service()

    mock_stock_service.get_available_stock.return_value = 0.0
    mock_producer_repo.get_by_id.return_value = {
        "id": 1,
        "name": "Test Producer",
        "email": "test@example.com",
    }
    mock_producer_repo.delete.return_value = True

    result = await service.delete_producer(1)

    assert result is True
    mock_producer_repo.delete.assert_called_once_with(1)


@pytest.mark.asyncio
async def test_delete_non_existent_producer():
    """Test that deleting a producer who doesn't exist raises ProducerNotFoundError."""
    service, mock_producer_repo, _ = create_mocked_producer_service()
    mock_producer_repo.get_by_id.return_value = None

    with pytest.raises(ProducerNotFoundError):
        await service.delete_producer(999)

    mock_producer_repo.get_by_id.assert_called_once_with(999)


@pytest.mark.asyncio
async def test_delete_producer_fails_at_repository():
    """Test the case where the repository fails to delete an existing producer."""
    service, mock_producer_repo, mock_stock_service = create_mocked_producer_service()

    mock_producer_repo.get_by_id.return_value = {
        "id": 1,
        "name": "Test Producer",
        "email": "test@example.com",
    }
    mock_stock_service.get_available_stock.return_value = 0.0

    mock_producer_repo.delete.return_value = False

    with pytest.raises(ProducerNotFoundError):
        await service.delete_producer(1)

    mock_producer_repo.delete.assert_called_once_with(1)
