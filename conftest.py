import pytest
import requests

from configs.config import BASE_URL


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="module")
def session():
    s = requests.Session()
    s.verify = False  # Avoid SSL errors
    return s