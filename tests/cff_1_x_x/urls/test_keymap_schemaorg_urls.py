# pylint:disable = protected-access
import types
import pytest
from cffconvert.cff_1_x_x.schemaorg_urls import SchemaorgUrls
from .get_every_key import get_every_key


@pytest.mark.parametrize("key", get_every_key())
def test_keys_schemaorg_urls(key):
    url = SchemaorgUrls({})
    assert key in url._behaviors
    assert isinstance(url._behaviors[key], (types.MethodType, types.FunctionType))


def test_number_of_keys():
    expected = len(get_every_key())
    actual = len(SchemaorgUrls({})._behaviors)
    assert actual == expected
