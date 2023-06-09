import enum


class IsothermModel(enum.Enum):
    LANGMUIR = "langmuir"


class IsothermType(enum.Enum):
    ABSOLUTE = "absolute"
    EXCESS = "excess"
    REDUCED = "reduced"
