from websorb.models.data_regression import IsothermData
from ._langmuir import LangmuirHandler
from ._abstract_handler import AbstractIsothermHandler


class IsothermHandlerNotFound(Exception):
    """"""


def get_isotherm_handler(data: IsothermData) -> AbstractIsothermHandler:
    if data.isotherm == "langmuir":
        return LangmuirHandler()
    else:
        raise IsothermHandlerNotFound(f"Handler for {data.isotherm} not found")
