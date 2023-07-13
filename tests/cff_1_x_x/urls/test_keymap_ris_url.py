import types
import pytest
from cffconvert.cff_1_x_x.ris_url import RisUrl
from .get_every_key import get_every_key


@pytest.mark.parametrize("key", get_every_key())
def test_keys_ris_url(key):
    url = RisUrl({})
    assert isinstance(url._behaviors[key], types.MethodType) or \
           isinstance(url._behaviors[key], types.FunctionType)


def test_number_of_keys():
    expected = len(get_every_key())
    actual = len(RisUrl({})._behaviors.keys())
    assert actual == expected
