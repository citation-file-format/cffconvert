# pylint:disable = protected-access
import types
import pytest
from cffconvert.cff_1_x_x.apalike_url import ApalikeUrl
from .get_every_key import get_every_key


@pytest.mark.parametrize("key", get_every_key())
def test_keys_apalike_url(key):
    url = ApalikeUrl({})
    assert key in url._behaviors
    assert isinstance(url._behaviors[key], (types.MethodType, types.FunctionType))


def test_number_of_keys():
    expected = len(get_every_key())
    actual = len(ApalikeUrl({})._behaviors)
    assert actual == expected