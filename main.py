from typing import Any, Dict
from fastapi import FastAPI, status
from websorb.views.isotherm_regression_view import isotherm_regression_router
from websorb.views.isotherm_calc_view import isotherm_calculation_router


app = FastAPI()

app.include_router(isotherm_regression_router)
app.include_router(isotherm_calculation_router)


@app.get("/", status_code=status.HTTP_200_OK)
def root() -> Dict[str, Any]:
    return {"message": "webSORB REST API running"}


# log_config = uvicorn.config.LOGGING_CONFIG
# log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
# log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

# uvicorn.run("app", reload=True)
