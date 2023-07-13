# pylint:disable = protected-access
import types
import pytest
from cffconvert.cff_1_x_x.schemaorg_author import SchemaorgAuthor
from .get_every_key import get_every_key


@pytest.mark.parametrize("key", get_every_key())
def test_keys_schemaorg_author(key):
    author = SchemaorgAuthor(author=None)
    assert key in author._behaviors
    assert isinstance(author._behaviors[key], (types.MethodType, types.FunctionType))


def test_number_of_keys():
    expected = len(get_every_key())
    actual = len(SchemaorgAuthor(author=None)._behaviors)
    assert actual == expected
