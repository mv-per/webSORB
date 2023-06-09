from fastapi.testclient import TestClient


import pytest


@pytest.fixture(scope="session", autouse=True)
def client() -> TestClient:
    from main import app

    return TestClient(app)
