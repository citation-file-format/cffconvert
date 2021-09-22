from abc import ABC


# pylint: disable=too-few-public-methods
class AbstractAuthorShared(ABC):

    def __init__(self, author):
        self._author = author
        self._behaviors = None

    @staticmethod
    def _from_thin_air():
        return None

    def _get_full_last_name(self):
        nameparts = [
            self._author.get('name-particle'),
            self._author.get('family-names'),
            self._author.get('name-suffix')
        ]
        return ' '.join([n for n in nameparts if n is not None])

    def _has_affiliation(self):
        value = self._author.get('affiliation', None)
        if value is not None and value != '':
            return 'A'
        return '_'

    def _has_alias(self):
        value = self._author.get('alias', None)
        if value is not None and value != '':
            return 'A'
        return '_'

    def _has_given_name(self):
        value = self._author.get('given-names', None)
        if value is not None and value != '':
            return 'G'
        return '_'

    def _has_family_name(self):
        value = self._author.get('family-names', None)
        if value is not None and value != '':
            return 'F'
        return '_'

    def _has_name(self):
        value = self._author.get('name', None)
        if value is not None and value != '':
            return 'N'
        return '_'

    def _has_orcid(self):
        value = self._author.get('orcid', None)
        if value is not None and value != '':
            return 'O'
        return '_'
