import pytest

from websorb.models.data_regression import IsothermDataRegression
from websorb.models.isotherm import IsothermModel
from websorb.numerical.isotherm_regression.regression import Regression


def test_regression_post_init_checks() -> None:
    isotherm_data = IsothermDataRegression(
        isotherm="some-unknown-isotherm",
        temperature=100,
        loadings=[1, 2, 3, 4],
        pressures=[4, 3, 2, 1],
    )

    with pytest.raises(AssertionError, match="Isotherm model not found"):
        Regression(isotherm_data)

    isotherm_data = IsothermDataRegression(
        isotherm=IsothermModel.LANGMUIR.value,
        temperature=100,
        loadings=[1, 2, 3],
        pressures=[4, 3, 2, 1],
    )

    with pytest.raises(
        AssertionError, match="Pressures and loadings must have the same length"
    ):
        Regression(isotherm_data)


def test_regression_run() -> None:
    isotherm_data = IsothermDataRegression(
        isotherm="langmuir",
        temperature=100,
        pressures=[1.82, 3.27, 7.12, 10.63, 15.92],
        loadings=[0.1208, 0.1919, 0.3432, 0.4519, 0.5849],
    )

    regression = Regression(isotherm_data)

    regression.optimize()
