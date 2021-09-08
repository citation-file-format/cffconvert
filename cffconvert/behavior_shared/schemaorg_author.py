from abc import abstractmethod


class SchemaorgAuthorShared:

    def __init__(self, author_cff):
        self._author_cff = author_cff
        self._behaviors = {
            'GFANAO': self._from_given_and_last_and_alias_and_name_and_affiliation_and_orcid,
            'GFANA.': self._from_given_and_last_and_alias_and_name_and_affiliation,
            'GFAN.O': self._from_given_and_last_and_alias_and_name_and_orcid,
            'GFAN..': self._from_given_and_last_and_alias_and_name,
            'GFA.AO': self._from_given_and_last_and_alias_and_affiliation_and_orcid,
            'GFA.A.': self._from_given_and_last_and_alias_and_affiliation,
            'GFA..O': self._from_given_and_last_and_alias_and_orcid,
            'GFA...': self._from_given_and_last_and_alias,
            'GF.NAO': self._from_given_and_last_and_name_and_affiliation_and_orcid,
            'GF.NA.': self._from_given_and_last_and_name_and_affiliation,
            'GF.N.O': self._from_given_and_last_and_name_and_orcid,
            'GF.N..': self._from_given_and_last_and_name,
            'GF..AO': self._from_given_and_last_and_affiliation_and_orcid,
            'GF..A.': self._from_given_and_last_and_affiliation,
            'GF...O': self._from_given_and_last_and_orcid,
            'GF....': self._from_given_and_last,
            'G.ANAO': self._from_given_and_alias_and_name_and_affiliation_and_orcid,
            'G.ANA.': self._from_given_and_alias_and_name_and_affiliation,
            'G.AN.O': self._from_given_and_alias_and_name_and_orcid,
            'G.AN..': self._from_given_and_alias_and_name,
            'G.A.AO': self._from_given_and_alias_and_affiliation_and_orcid,
            'G.A.A.': self._from_given_and_alias_and_affiliation,
            'G.A..O': self._from_given_and_alias_and_orcid,
            'G.A...': self._from_given_and_alias,
            'G..NAO': self._from_given_and_name_and_affiliation_and_orcid,
            'G..NA.': self._from_given_and_name_and_affiliation,
            'G..N.O': self._from_given_and_name_and_orcid,
            'G..N..': self._from_given_and_name,
            'G...AO': self._from_given_and_affiliation_and_orcid,
            'G...A.': self._from_given_and_affiliation,
            'G....O': self._from_given_and_orcid,
            'G.....': self._from_given,
            '.FANAO': self._from_last_and_alias_and_name_and_affiliation_and_orcid,
            '.FANA.': self._from_last_and_alias_and_name_and_affiliation,
            '.FAN.O': self._from_last_and_alias_and_name_and_orcid,
            '.FAN..': self._from_last_and_alias_and_name,
            '.FA.AO': self._from_last_and_alias_and_affiliation_and_orcid,
            '.FA.A.': self._from_last_and_alias_and_affiliation,
            '.FA..O': self._from_last_and_alias_and_orcid,
            '.FA...': self._from_last_and_alias,
            '.F.NAO': self._from_last_and_name_and_affiliation_and_orcid,
            '.F.NA.': self._from_last_and_name_and_affiliation,
            '.F.N.O': self._from_last_and_name_and_orcid,
            '.F.N..': self._from_last_and_name,
            '.F..AO': self._from_last_and_affiliation_and_orcid,
            '.F..A.': self._from_last_and_affiliation,
            '.F...O': self._from_last_and_orcid,
            '.F....': self._from_last,
            '..ANAO': self._from_alias_and_name_and_affiliation_and_orcid,
            '..ANA.': self._from_alias_and_name_and_affiliation,
            '..AN.O': self._from_alias_and_name_and_orcid,
            '..AN..': self._from_alias_and_name,
            '..A.AO': self._from_alias_and_affiliation_and_orcid,
            '..A.A.': self._from_alias_and_affiliation,
            '..A..O': self._from_alias_and_orcid,
            '..A...': self._from_alias,
            '...NAO': self._from_name_and_affiliation_and_orcid,
            '...NA.': self._from_name_and_affiliation,
            '...N.O': self._from_name_and_orcid,
            '...N..': self._from_name,
            '....AO': self._from_affiliation_and_orcid,
            '....A.': self._from_affiliation,
            '.....O': self._from_orcid,
            '......': SchemaorgAuthorShared._from_thin_air
        }

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
            'alternateName': self._author_cff.get('alias')
        }

    def _from_alias_and_affiliation(self):
        return {
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            }
        }

    def _from_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            }
        }

    def _from_alias_and_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'name': self._author_cff.get('name')
        }

    def _from_alias_and_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'name': self._author_cff.get('name')
        }

    def _from_alias_and_name_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'name': self._author_cff.get('name')
        }

    def _from_alias_and_name(self):
        return {
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'name': self._author_cff.get('name')
        }

    def _from_alias_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias')
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

    def _from_given_and_alias(self):
        return {
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_alias_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_alias_and_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_alias_and_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_alias_and_name_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_alias_and_name(self):
        return {
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_alias_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
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

    def _from_given_and_last_and_alias(self):
        return {
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_last_and_alias_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_last_and_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_last_and_alias_and_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_last_and_alias_and_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_last_and_alias_and_name_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_last_and_alias_and_name(self):
        return {
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_last_and_alias_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_last_and_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_last_and_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_last_and_name_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_last_and_name(self):
        return {
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_last_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'givenName': self._author_cff.get('given-names')
        }

    def _from_given_and_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_name_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
        }

    def _from_given_and_name(self):
        return {
            '@type': 'Person',
            'givenName': self._author_cff.get('given-names'),
            'name': self._author_cff.get('name')
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

    def _from_last_and_alias(self):
        return {
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_alias_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_alias_and_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'name': self._author_cff.get('name')
        }

    def _from_last_and_alias_and_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'name': self._author_cff.get('name')
        }

    def _from_last_and_alias_and_name_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'name': self._author_cff.get('name')
        }

    def _from_last_and_alias_and_name(self):
        return {
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name(),
            'name': self._author_cff.get('name')
        }

    def _from_last_and_alias_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author_cff.get('alias'),
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'name': self._author_cff.get('name')
        }

    def _from_last_and_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'name': self._author_cff.get('name')
        }

    def _from_last_and_name_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'name': self._author_cff.get('name')
        }

    def _from_last_and_name(self):
        return {
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'name': self._author_cff.get('name')
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

    @abstractmethod
    def as_dict(self):
        pass
