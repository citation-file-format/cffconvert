import types
import pytest
from cffconvert.cff_1_x_x.apalike_url import ApalikeUrl
from .get_every_key import get_every_key


@pytest.mark.parametrize("key", get_every_key())
def test_keys_apalike_url(key):
    url = ApalikeUrl({})
    assert isinstance(url._behaviors[key], types.MethodType) or \
           isinstance(url._behaviors[key], types.FunctionType)


def test_number_of_keys():
    expected = len(get_every_key())
    actual = len(ApalikeUrl({})._behaviors.keys())
    assert actual == expected
