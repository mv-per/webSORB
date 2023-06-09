import logging
from typing import Dict, List
from websorb.models.data_regression import IsothermData, IsothermDataRegression

from websorb.numerical.isotherm_handlers._abstract_handler import (
    AbstractIsothermHandler,
)


class LangmuirHandler(AbstractIsothermHandler):
    PARAMETERS = ["n_max", "k"]
    _logger = logging.getLogger("LangmuirHandler")

    def get_loading(self, pressure: float, parameters: list[float]) -> float:
        n_max, k = parameters
        return n_max * k * pressure / (1.0 + k * pressure)

    def get_loadings(
        self, pressures: list[float], parameters: list[float]
    ) -> list[float]:
        n_max, k = parameters
        return [n_max * k * P / (1.0 + k * P) for P in pressures]

    def get_initial_estimates(
        self, isotherm_data: IsothermDataRegression
    ) -> list[float]:
        if isotherm_data.initial_estimates is not None:
            return [
                isotherm_data.initial_estimates["n_max"],
                isotherm_data.initial_estimates["k"],
            ]

        return [max(isotherm_data.loadings), 0.05]

    def get_parameters(self, isotherm_data: IsothermData) -> list[float]:
        if isotherm_data.parameters is None:
            raise Exception("lalalla")
        return [
            isotherm_data.parameters["n_max"],
            isotherm_data.parameters["k"],
        ]

    def convert_parameters_to_dict(self, parameters: List[float]) -> Dict[str, float]:
        return dict(zip(self.PARAMETERS, parameters))

    def check_initial_estimates(self, isotherm_data: IsothermDataRegression) -> None:
        if isotherm_data.initial_estimates is None:
            self._logger.info(
                "Initial estimates check should only run in models wirh initial estimates"
            )
            return

        for parameter in self.PARAMETERS:
            assert (
                parameter in isotherm_data.initial_estimates.keys()
            ), f"""Missing parameter {parameter} from initial estimates. 
                    Required parameters = {self.PARAMETERS}"""
