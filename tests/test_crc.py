import pytest
from redis_sacsc.crc import crc64


@pytest.mark.parametrize(("first", "expected"), [("foo", 12626267673720558670)])
def test_some_function(first, expected):
    """Example test with parametrization."""
    assert crc64(first) == expected
