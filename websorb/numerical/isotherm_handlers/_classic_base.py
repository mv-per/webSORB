from logging import Logger
from typing import Dict, List

from ClassicIsotherms import ClassicIsotherms

from websorb.models.data_regression import IsothermData, IsothermDataRegression
from websorb.numerical.isotherm_handlers._abstract_handler import (
    AbstractIsothermHandler,
)


class ClassicIsothermHandlersBase(AbstractIsothermHandler):
    _isotherm: ClassicIsotherms
    _parameters: list[str]
    _logger: Logger

    def get_loading(
        self, pressure: float, temperature: float, parameters: list[float]
    ) -> float:
        return self._isotherm.get_loading(  # type:ignore[no-any-return]
            pressure, temperature, parameters
        )

    def get_loadings(
        self, pressures: list[float], temperature: float, parameters: list[float]
    ) -> list[float]:
        return self._isotherm.get_loadings(  # type:ignore[no-any-return]
            pressures, temperature, parameters
        )

    def get_deviation(
        self,
        pressures: list[float],
        experimental_loadings: list[float],
        temperature: float,
        parameters: list[float],
        deviation_equation: str,
    ) -> float:
        return self._isotherm.get_deviation(  # type:ignore[no-any-return]
            pressures,
            experimental_loadings,
            temperature,
            parameters,
            deviation_equation,
        )

    def convert_parameters_to_dict(self, parameters: List[float]) -> Dict[str, float]:
        return dict(zip(self._parameters, parameters))

    def check_initial_estimates(self, isotherm_data: IsothermDataRegression) -> None:
        if isotherm_data.initial_estimates is None:
            self._logger.info(
                "Initial estimates check should only run in models wirh initial estimates"
            )
            return

        for parameter in self._parameters:
            assert (
                parameter in isotherm_data.initial_estimates.keys()
            ), f"""Missing parameter {parameter} from initial estimates.
                    Required parameters = {self._parameters}"""

    def get_initial_estimates(
        self, isotherm_data: IsothermDataRegression
    ) -> list[float]:
        raise NotImplementedError()

    def get_parameters(self, isotherm_data: IsothermData) -> list[float]:
        raise NotImplementedError()
