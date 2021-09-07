import json
from abc import abstractmethod


class SchemaorgAuthorShared:

    def __init__(self, author_cff):
        self._author_cff = author_cff
        self._behaviors = None

    def _exists_nonempty(self, key):
        value = self._author_cff.get(key, None)
        return value is not None and value != ''

    def _from_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            }
        }

    def _from_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            }
        }

    def _from_alias(self):
        return {
            '@type': 'Person',
            'name': self._author_cff.get('alias')
        }

    def _from_alias_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'name': self._author_cff.get('alias')
        }

    def _from_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'name': self._author_cff.get('alias')
        }

    def _from_alias_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'name': self._author_cff.get('alias')
        }

    def _from_given(self):
        return {
            '@type': 'Person',
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_last(self):
        return {
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_last_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_last_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_last_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'givenName': self._author_cff.get('given-names')
        }

    def _from_last(self):
        return {
            '@type': 'Person',
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'familyName': self._get_full_last_name()
        }

    def _from_name(self):
        return {
            '@type': 'Person',
            'name': self._author_cff.get('name')
        }

    def _from_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'name': self._author_cff.get('name')
        }

    def _from_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'name': self._author_cff.get('name')
        }

    def _from_name_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'name': self._author_cff.get('name')
        }

    def _from_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person'
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

    def as_dict(self):
        state = [
            self._exists_nonempty('given-names'),
            self._exists_nonempty('family-names'),
            self._exists_nonempty('alias'),
            self._exists_nonempty('name'),
            self._exists_nonempty('affiliation'),
            self._exists_nonempty('orcid')
        ]
        key = ''.join(['T' if item is True else 'F' for item in state])
        return self._behaviors[key]()
