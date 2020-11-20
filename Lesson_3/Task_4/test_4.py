from armstrong import is_armstrong

import pytest


@pytest.mark.parametrize(
    ("value"),
    [
        (153),
        (407),
        (5),
    ],
)
def test_value_is_armstrong(value: int):
    assert is_armstrong(value) is True


@pytest.mark.parametrize(
    ("value"),
    [
        (10),
        (320),
        (1630),
    ],
)
def test_value_is_not_armstrong(value: int):
    assert is_armstrong(value) is False
