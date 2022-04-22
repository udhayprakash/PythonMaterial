from dataclasses import KW_ONLY, dataclass, field
from datetime import datetime


@dataclass(kw_only=True)
class Birthday:
    name: str
    birthday: datetime.date


@dataclass
class Birthday2:
    name: str
    birthday: datetime.date = field(kw_only=True)


@dataclass
class Point:
    x: float
    y: float
    _: KW_ONLY
    z: float = 0.0
    t: float = 0.0
