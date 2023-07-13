import itertools
import types
import pytest
from cffconvert.behavior_1_2_x.bibtex_author import BibtexAuthor


def get_every_key():
    given_name_values = ["G", "_"]
    family_name_values = ["F", "_"]
    alias_values = ["A", "_"]
    name_values = ["N", "_"]
    combined = [
        given_name_values,
        family_name_values,
        alias_values,
        name_values
    ]
    return ["".join(combo) for combo in itertools.product(*combined)]


@pytest.mark.parametrize("key", get_every_key())
def test_keys_bibtex_author(key):
    author = BibtexAuthor(author=None)
    assert isinstance(author._behaviors[key], types.MethodType) or \
           isinstance(author._behaviors[key], types.FunctionType)


def test_number_of_keys():
    expected = len(get_every_key())
    actual = len(BibtexAuthor(author=None)._behaviors.keys())
    assert actual == expected
