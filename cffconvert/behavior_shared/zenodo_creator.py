from abc import abstractmethod


class ZenodoCreatorShared:

    def __init__(self, author_cff):
        self._author_cff = author_cff
        self._behaviors = None

    def _exists_nonempty(self, key):
        value = self._author_cff.get(key, None)
        return value is not None and value != ''

    def _from_affiliation(self):
        return {
            'affiliation': self._author_cff.get('affiliation')
        }

    def _from_affiliation_and_orcid(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_alias(self):
        return {
            'name': self._author_cff.get('alias')
        }

    def _from_alias_and_affiliation(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._author_cff.get('alias')
        }

    def _from_alias_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._author_cff.get('alias'),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_alias_and_orcid(self):
        return {
            'name': self._author_cff.get('alias'),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_given(self):
        return {
            'name': self._author_cff.get('given-names')
        }

    def _from_given_and_affiliation(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._author_cff.get('given-names')
        }

    def _from_given_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._author_cff.get('given-names'),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_given_and_last(self):
        return {
            'name': self._get_full_last_name() + ', ' + self._author_cff.get('given-names')
        }

    def _from_given_and_last_and_affiliation(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._get_full_last_name() + ', ' + self._author_cff.get('given-names')
        }

    def _from_given_and_last_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._get_full_last_name() + ', ' + self._author_cff.get('given-names'),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_given_and_last_and_orcid(self):
        return {
            'name': self._get_full_last_name() + ', ' + self._author_cff.get('given-names'),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_given_and_orcid(self):
        return {
            'name': self._author_cff.get('given-names'),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_last(self):
        return {
            'name': self._get_full_last_name()
        }

    def _from_last_and_affiliation(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._get_full_last_name()
        }

    def _from_last_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._get_full_last_name(),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_last_and_orcid(self):
        return {
            'name': self._get_full_last_name(),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_name(self):
        return {
            'name': self._author_cff.get('name')
        }

    def _from_name_and_affiliation(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._author_cff.get('name')
        }

    def _from_name_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author_cff.get('affiliation'),
            'name': self._author_cff.get('name'),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_name_and_orcid(self):
        return {
            'name': self._author_cff.get('name'),
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    def _from_orcid(self):
        return {
            'orcid': self._author_cff.get('orcid').replace('https://orcid.org/', '')
        }

    @staticmethod
    def _from_thin_air():
        return None

    def _get_full_last_name(self):
        nameparts = [
            self._author_cff.get('name-particle'),
            self._author_cff.get('family-names'),
            self._author_cff.get('name-suffix')
        ]
        return ' '.join([n for n in nameparts if n is not None])

    @abstractmethod
    def as_dict(self):
        pass
