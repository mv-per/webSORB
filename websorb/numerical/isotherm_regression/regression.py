import logging
from typing import Any, Dict

import attr
import numpy
from scipy.optimize import minimize

from websorb.models.data_regression import IsothermDataRegression
from websorb.models.isotherm import IsothermModel
from websorb.numerical.isotherm_handlers import AbstractIsothermHandler
from websorb.numerical.isotherm_handlers.helpers import get_isotherm_handler


class OptimizationError(Exception):
    """"""


@attr.s
class Regression:
    isotherm_data: IsothermDataRegression = attr.ib()

    isotherm_handler: AbstractIsothermHandler = attr.ib(default=None, init=False)

    def __attrs_post_init__(self) -> None:
        self._logger = logging.getLogger("Regression")
        self.check_isotherm_data()

    def optimize(self) -> IsothermDataRegression:
        initial_estimates = self.isotherm_handler.get_initial_estimates(
            self.isotherm_data
        )

        def objective_function(estimates: list[float]) -> float:
            return self.isotherm_handler.get_deviation(  # type:ignore[no-any-return]
                self.isotherm_data.pressures,
                self.isotherm_data.loadings,
                self.isotherm_data.temperature,
                estimates,
                self.isotherm_data.deviation_equation,
            )

        optimization = minimize(
            objective_function, initial_estimates, method="Nelder-Mead"
        )

        self.post_run_check(optimization)

        return self.isotherm_data

    def get_diff(self, n_exp: float, n_calc: float) -> float:
        return float(numpy.abs(n_exp - n_calc))

    def check_isotherm_data(self) -> None:
        isotherms = [member.value for member in IsothermModel]
        assert self.isotherm_data.isotherm in isotherms, "Isotherm model not found"

        assert len(self.isotherm_data.loadings) == len(
            self.isotherm_data.pressures
        ), "Pressures and loadings must have the same length"

        self.isotherm_handler = get_isotherm_handler(self.isotherm_data)

        if self.isotherm_data.initial_estimates is not None:
            self.isotherm_handler.check_initial_estimates(self.isotherm_data)

    def post_run_check(self, optimization: Dict[str, Any]) -> None:
        if not optimization["success"]:
            raise OptimizationError("Error optimizing data")

        self.isotherm_data.parameters = (
            self.isotherm_handler.convert_parameters_to_dict(optimization["x"])
        )
