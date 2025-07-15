def test_read_producers(test_producer_client):
    client, _ = test_producer_client
    response = client.get("/producers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_producer(test_producer_client):
    client, _ = test_producer_client
    response = client.post(
        "/producers/",
        json={"name": "Integration Test Producer", "email": "integration@test.com"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Integration Test Producer"
    assert "id" in data


def test_read_producer(test_producer_client):
    client, _ = test_producer_client
    response = client.post(
        "/producers/", json={"name": "Another Producer", "email": "another@test.com"}
    )
    producer_id = response.json()["id"]

    response = client.get(f"/producers/{producer_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Another Producer"


def test_update_producer(test_producer_client):
    client, _ = test_producer_client
    response = client.post(
        "/producers/", json={"name": "Producer to Update", "email": "update@test.com"}
    )
    producer_id = response.json()["id"]

    response = client.put(f"/producers/{producer_id}", json={"name": "Updated Name"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Name"


def test_delete_producer(test_producer_client):
    client, mock_stock_service = test_producer_client
    response = client.post(
        "/producers/", json={"name": "Producer to Delete", "email": "delete@test.com"}
    )
    producer_id = response.json()["id"]

    mock_stock_service.get_available_stock.return_value = 0.0

    response = client.delete(f"/producers/{producer_id}")
    assert response.status_code == 202

    response = client.get(f"/producers/{producer_id}")
    assert response.status_code == 404


def test_read_non_existent_producer(test_producer_client):
    client, _ = test_producer_client
    response = client.get("/producers/999")
    assert response.status_code == 404


def test_update_non_existent_producer(test_producer_client):
    client, _ = test_producer_client
    response = client.put("/producers/999", json={"name": "New Name"})
    assert response.status_code == 404


def test_delete_producer_with_stock(test_producer_client):
    client, mock_stock_service = test_producer_client
    response = client.post(
        "/producers/", json={"name": "Producer With Stock", "email": "stock@test.com"}
    )
    producer_id = response.json()["id"]
    mock_stock_service.get_available_stock.return_value = 10.0
    response = client.delete(f"/producers/{producer_id}")
    assert response.status_code == 400
    data = response.json()
    assert "cannot be deleted" in data["detail"]
    mock_stock_service.get_available_stock.return_value = 0.0


def test_create_producer_with_invalid_email(test_producer_client):
    client, _ = test_producer_client
    response = client.post(
        "/producers/", json={"name": "Bad Email Producer", "email": "not-an-email"}
    )
    assert response.status_code == 422
