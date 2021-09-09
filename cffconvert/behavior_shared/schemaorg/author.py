from abc import abstractmethod


class SchemaorgAuthorShared:

    def __init__(self, author_cff):
        self._author_cff = author_cff
        self._behaviors = {
            'GFANAO': self._from_given_and_last_and_alias_and_name_and_affiliation_and_orcid,
            'GFANA_': self._from_given_and_last_and_alias_and_name_and_affiliation,
            'GFAN_O': self._from_given_and_last_and_alias_and_name_and_orcid,
            'GFAN__': self._from_given_and_last_and_alias_and_name,
            'GFA_AO': self._from_given_and_last_and_alias_and_affiliation_and_orcid,
            'GFA_A_': self._from_given_and_last_and_alias_and_affiliation,
            'GFA__O': self._from_given_and_last_and_alias_and_orcid,
            'GFA___': self._from_given_and_last_and_alias,
            'GF_NAO': self._from_given_and_last_and_name_and_affiliation_and_orcid,
            'GF_NA_': self._from_given_and_last_and_name_and_affiliation,
            'GF_N_O': self._from_given_and_last_and_name_and_orcid,
            'GF_N__': self._from_given_and_last_and_name,
            'GF__AO': self._from_given_and_last_and_affiliation_and_orcid,
            'GF__A_': self._from_given_and_last_and_affiliation,
            'GF___O': self._from_given_and_last_and_orcid,
            'GF____': self._from_given_and_last,
            'G_ANAO': self._from_given_and_alias_and_name_and_affiliation_and_orcid,
            'G_ANA_': self._from_given_and_alias_and_name_and_affiliation,
            'G_AN_O': self._from_given_and_alias_and_name_and_orcid,
            'G_AN__': self._from_given_and_alias_and_name,
            'G_A_AO': self._from_given_and_alias_and_affiliation_and_orcid,
            'G_A_A_': self._from_given_and_alias_and_affiliation,
            'G_A__O': self._from_given_and_alias_and_orcid,
            'G_A___': self._from_given_and_alias,
            'G__NAO': self._from_given_and_name_and_affiliation_and_orcid,
            'G__NA_': self._from_given_and_name_and_affiliation,
            'G__N_O': self._from_given_and_name_and_orcid,
            'G__N__': self._from_given_and_name,
            'G___AO': self._from_given_and_affiliation_and_orcid,
            'G___A_': self._from_given_and_affiliation,
            'G____O': self._from_given_and_orcid,
            'G_____': self._from_given,
            '_FANAO': self._from_last_and_alias_and_name_and_affiliation_and_orcid,
            '_FANA_': self._from_last_and_alias_and_name_and_affiliation,
            '_FAN_O': self._from_last_and_alias_and_name_and_orcid,
            '_FAN__': self._from_last_and_alias_and_name,
            '_FA_AO': self._from_last_and_alias_and_affiliation_and_orcid,
            '_FA_A_': self._from_last_and_alias_and_affiliation,
            '_FA__O': self._from_last_and_alias_and_orcid,
            '_FA___': self._from_last_and_alias,
            '_F_NAO': self._from_last_and_name_and_affiliation_and_orcid,
            '_F_NA_': self._from_last_and_name_and_affiliation,
            '_F_N_O': self._from_last_and_name_and_orcid,
            '_F_N__': self._from_last_and_name,
            '_F__AO': self._from_last_and_affiliation_and_orcid,
            '_F__A_': self._from_last_and_affiliation,
            '_F___O': self._from_last_and_orcid,
            '_F____': self._from_last,
            '__ANAO': self._from_alias_and_name_and_affiliation_and_orcid,
            '__ANA_': self._from_alias_and_name_and_affiliation,
            '__AN_O': self._from_alias_and_name_and_orcid,
            '__AN__': self._from_alias_and_name,
            '__A_AO': self._from_alias_and_affiliation_and_orcid,
            '__A_A_': self._from_alias_and_affiliation,
            '__A__O': self._from_alias_and_orcid,
            '__A___': self._from_alias,
            '___NAO': self._from_name_and_affiliation_and_orcid,
            '___NA_': self._from_name_and_affiliation,
            '___N_O': self._from_name_and_orcid,
            '___N__': self._from_name,
            '____AO': self._from_affiliation_and_orcid,
            '____A_': self._from_affiliation,
            '_____O': self._from_orcid,
            '______': SchemaorgAuthorShared._from_thin_air
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
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
        }

    def _from_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author_cff.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author_cff.get('affiliation')
            },
            'alternateName': self._author_cff.get('alias'),
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
