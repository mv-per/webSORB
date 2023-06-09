import pytest
from websorb.models.data_regression import IsothermDataRegression
from websorb.numerical.isotherm_handlers._langmuir import LangmuirHandler


@pytest.fixture
def handler() -> LangmuirHandler:
    return LangmuirHandler()


@pytest.fixture
def data() -> IsothermDataRegression:
    return IsothermDataRegression(
        isotherm="langmuir", loadings=[1, 2, 4.444], pressures=[3, 2, 1]
    )


def test_get_loading(handler: LangmuirHandler) -> None:
    loading = handler.get_loading(1000, [2.3, 0.05])
    assert pytest.approx(loading) == 2.25490


def test_get_loadings(handler: LangmuirHandler) -> None:
    loadings = handler.get_loadings([1, 30, 100], [2.3, 0.05])
    print(loadings)
    expected = [0.10952380952380951, 1.38, 1.9166666666666667]
    assert all(
        [
            pytest.approx(loading) == expect
            for loading, expect in zip(loadings, expected)
        ]
    )


def test_get_initial_estimates(
    handler: LangmuirHandler, data: IsothermDataRegression
) -> None:
    original_estimates = {"n_max": 3, "k": 0.05}
    data.initial_estimates = original_estimates

    estimates = handler.get_initial_estimates(data)

    assert estimates == [3, 0.05]

    serialized_estimates = handler.convert_parameters_to_dict(estimates)

    assert serialized_estimates == original_estimates


def test_get_initial_estimates_default(
    handler: LangmuirHandler, data: IsothermDataRegression
) -> None:
    estimates = handler.get_initial_estimates(data)

    assert estimates == [4.444, 0.05]


def test_check_estimates_fail(
    handler: LangmuirHandler, data: IsothermDataRegression
) -> None:
    data.initial_estimates = {"k": 0.44}

    with pytest.raises(AssertionError, match=""):
        handler.check_initial_estimates(data)
