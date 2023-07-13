import types
import pytest
from cffconvert.cff_1_x_x.apalike_author import ApalikeAuthor
from .get_every_key import get_every_key


@pytest.mark.parametrize("key", get_every_key())
def test_keys_apalike_author(key):
    author = ApalikeAuthor(author=None)
    assert key in author._behaviors.keys()
    assert isinstance(author._behaviors[key], types.MethodType) or \
           isinstance(author._behaviors[key], types.FunctionType)


def test_number_of_keys():
    expected = len(get_every_key())
    actual = len(ApalikeAuthor(author=None)._behaviors.keys())
    assert actual == expected
