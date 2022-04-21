import flatdict
import pandas as pd
from collections.abc import MutableMapping

# ======= method - 1


def flatten_dict(
    d: MutableMapping, parent_key: str = "", sep: str = "."
) -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


# ====== method - 2


def _flatten_dict_gen(d, parent_key, sep):
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            yield from flatten_dict(v, new_key, sep=sep).items()
        else:
            yield new_key, v


def flatten_dict(d: MutableMapping, parent_key: str = "", sep: str = "."):
    return dict(_flatten_dict_gen(d, parent_key, sep))


# ====== method - 3


def flatten_dict(d: MutableMapping, sep: str = ".") -> MutableMapping:
    [flat_dict] = pd.json_normalize(d, sep=sep).to_dict(orient="records")
    return flat_dict


print(
    flatten_dict({"a": 1, "c": {"a": 2, "b": {"x": 3, "y": 4, "z": 5}}, "d": [6, 7, 8]})
)
# {'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}


# method - 4 -- using flatdict module
print(
    flatdict.FlatDict(
        {"a": 1, "c": {"a": 2, "b": {"x": 3, "y": 4, "z": 5}}, "d": [6, 7, 8]},
        delimiter=".",
    )
)

# collections.abc
# ------------------
# 'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
# 'ByteString',
# 'Callable', 'Collection', 'Container', 'Coroutine',
# 'Generator',
# 'Hashable',
# 'ItemsView', 'Iterable', 'Iterator',
# 'KeysView',
# 'Mapping', 'MappingView', 'MutableMapping', 'MutableSequence', 'MutableSet',
# 'Reversible',
# 'Sequence', 'Set', 'Sized',
# 'ValuesView'
