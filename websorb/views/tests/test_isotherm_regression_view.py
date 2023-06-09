from fastapi.testclient import TestClient

from websorb.models.data_regression import IsothermDataRegression


def test_read_main(client: TestClient) -> None:
    regression_data = IsothermDataRegression(
        isotherm="langmuir",
        pressures=[1.82, 3.27, 7.12, 10.63, 15.92],
        loadings=[0.1208, 0.1919, 0.3432, 0.4519, 0.5849],
    )

    assert regression_data.parameters is None
    response = client.post("/isotherm-regression", json=regression_data.dict())
    assert response.status_code == 200

    assert response.json()["parameters"] == {
        "k": 0.047437256822305256,
        "n_max": 1.3593861618556966,
    }
