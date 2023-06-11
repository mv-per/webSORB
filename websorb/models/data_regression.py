from typing import Dict, Tuple

from pydantic import BaseModel

from websorb.models.isotherm import IsothermType


class IsothermData(BaseModel):  # type:ignore[misc]
    isotherm: str
    temperature: float
    pressures: list[float] = []
    loadings: list[float] = []
    parameters: Dict[str, float] | None = None
    isotherm_type: IsothermType | None = None


class IsothermDataRegression(IsothermData):
    initial_estimates: Dict[str, float] | None = None
    optimization_algorithm: str | None = "Nelder-Mead"
    deviation_equation: str | None = "SSE"


class IsothermDataCalculation(IsothermData):
    pressure_range: Tuple[float, float, int] | None = None
    temperature_range: Tuple[float, float, int] | None = None
