from fastapi import APIRouter, HTTPException
import numpy
from websorb.models.data_regression import (
    IsothermDataCalculation,
)
from fastapi import status
from websorb.numerical.isotherm_handlers import get_isotherm_handler

isotherm_calculation_router = APIRouter(
    prefix="/isotherm",
    tags=["IsothermModel Calculation"],
    responses={404: {"description": "Not Found"}},
)


@isotherm_calculation_router.post("/")
async def calculate(data: IsothermDataCalculation) -> IsothermDataCalculation:
    isotherm_handler = get_isotherm_handler(data)

    if isotherm_handler is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Handler for {data.isotherm} not found",
        )

    if data.pressure_range is not None:
        start, stop, points = data.pressure_range
        data.pressures = numpy.linspace(start, stop, points).tolist()

    parameters = isotherm_handler.get_parameters(data)
    data.loadings = isotherm_handler.get_loadings(data.pressures, parameters)
    return data
