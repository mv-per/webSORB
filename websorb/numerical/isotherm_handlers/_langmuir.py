import logging

from ClassicIsotherms import ClassicIsotherms

from websorb.models.data_regression import IsothermData, IsothermDataRegression
from websorb.numerical.isotherm_handlers._classic_base import (
    ClassicIsothermHandlersBase,
)


class LangmuirHandler(ClassicIsothermHandlersBase):
    def __init__(self) -> None:
        self._parameters = ["n_max", "b"]
        self._logger = logging.getLogger("LangmuirHandler")
        self._isotherm = ClassicIsotherms("langmuir")

    def get_initial_estimates(
        self, isotherm_data: IsothermDataRegression
    ) -> list[float]:
        if isotherm_data.initial_estimates is not None:
            return [
                isotherm_data.initial_estimates["n_max"],
                isotherm_data.initial_estimates["b"],
            ]

        return [max(isotherm_data.loadings), 0.05]

    def get_parameters(self, isotherm_data: IsothermData) -> list[float]:
        if isotherm_data.parameters is None:
            raise Exception("Parameters not found")
        return [
            isotherm_data.parameters["n_max"],
            isotherm_data.parameters["b"],
        ]
