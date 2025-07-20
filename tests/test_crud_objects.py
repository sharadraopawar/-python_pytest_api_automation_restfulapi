import pytest
from configs import config
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="module")
def created_object(session, base_url):
    payload = {
        "name": "MacBook Pro 16",
        "data": {
            "year": 2023,
            "price": "2400 USD",
            "CPU model": "M2 Max",
            "Hard disk size": "1 TB"
        }
    }

    response = session.post(base_url + config.OBJECTS_ENDPOINT, json=payload)
    assert response.status_code == 200
    object_id = response.json()["id"]
    logger.info(f"Created object with ID: {object_id}")
    return object_id

def test_get_single_object(session, base_url, created_object):
    response = session.get(f"{base_url}{config.OBJECTS_ENDPOINT}/{created_object}")
    logger.info(f"GET one - Status: {response.status_code}")
    assert response.status_code == 200
    assert response.json()["id"] == created_object

def test_update_object(session, base_url, created_object):
    update_payload = {
        "name": "MacBook Pro 16 Updated",
        "data": {
            "year": 2024,
            "price": "2500 USD"
        }
    }
    response = session.put(f"{base_url}{config.OBJECTS_ENDPOINT}/{created_object}", json=update_payload)
    logger.info(f"PUT update - Status: {response.status_code}")
    assert response.status_code == 200
    assert response.json()["name"] == "MacBook Pro 16 Updated"

def test_delete_object(session, base_url, created_object):
    response = session.delete(f"{base_url}{config.OBJECTS_ENDPOINT}/{created_object}")
    logger.info(f" DELETE - Status: {response.status_code}")
    assert response.status_code == 200
