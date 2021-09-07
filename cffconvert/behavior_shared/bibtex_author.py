from abc import abstractmethod


class BibtexAuthorShared:

    def __init__(self, author_cff):
        self._author_cff = author_cff
        self._behaviors = None

    def _exists_nonempty(self, key):
        value = self._author_cff.get(key, None)
        return value is not None and value != ''

    def _from_alias(self):
        return self._author_cff.get('alias')

    def _from_given_and_last(self):
        return self._from_last() + ", " + self._from_given()

    def _from_given(self):
        return self._author_cff.get('given-names')

    def _from_last(self):
        nameparts = [
            self._author_cff.get('name-particle'),
            self._author_cff.get('family-names'),
            self._author_cff.get('name-suffix')
        ]
        return ' '.join([n for n in nameparts if n is not None])

    def _from_name(self):
        return self._author_cff.get('name')

    @staticmethod
    def _from_thin_air():
        return None

    @abstractmethod
    def as_string(self):
        pass
