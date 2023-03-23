import warnings

import pytest


def api_call_v2():
    warnings.warn("use v3 of this api", DeprecationWarning)
    return 200


# api_call_v2()

with pytest.deprecated_call():
    assert api_call_v2() == 200


with pytest.warns(UserWarning, match="must be 0 or None"):
    warnings.warn("value must be 0 or None", UserWarning)

with pytest.warns(UserWarning, match=r"must be \d+$"):
    warnings.warn("value must be 42", UserWarning)

with pytest.warns(UserWarning, match=r"this is not here"):
    warnings.warn("this is not here", UserWarning)
