from fastapi import APIRouter
from websorb.models.data_regression import IsothermDataRegression
from websorb.numerical.isotherm_regression.regression import Regression

isotherm_regression_router = APIRouter(
    prefix="/isotherm-regression",
    tags=["IsothermModel Regression"],
    responses={404: {"description": "Not Found"}},
)


@isotherm_regression_router.post("/")
async def regression(data: IsothermDataRegression) -> IsothermDataRegression:
    regression = Regression(data)
    result = regression.optimize()
    return result
