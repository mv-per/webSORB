from typing import Dict, List, Protocol

from websorb.models.data_regression import IsothermData, IsothermDataRegression


class AbstractIsothermHandler(Protocol):
    def get_loading(
        self, pressure: float, temperature: float, parameters: List[float]
    ) -> float:
        ...  # pragma:no cover

    def get_loadings(
        self, pressures: List[float], temperature: float, parameters: List[float]
    ) -> List[float]:
        ...  # pragma:no cover

    def convert_parameters_to_dict(self, parameters: List[float]) -> Dict[str, float]:
        ...  # pragma:no cover

    def get_initial_estimates(
        self, data_regression: IsothermDataRegression
    ) -> List[float]:
        ...  # pragma:no cover

    def check_initial_estimates(self, data_regression: IsothermDataRegression) -> None:
        ...  # pragma:no cover

    def get_parameters(self, isotherm_data: IsothermData) -> list[float]:
        ...  # pragma:no cover

    def get_deviation(
        self,
        pressures: list[float],
        experimental_loadings: list[float],
        temperature: float,
        parameters: list[float],
        deviation_equation: str,
    ) -> float:
        ...  # pragma:no cover
