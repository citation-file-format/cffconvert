from cffconvert.behavior_1_x_x.abstract_author_shared import AbstractAuthorShared


# pylint: disable=too-few-public-methods
class SchemaorgAuthor(AbstractAuthorShared):

    def __init__(self, author):
        super().__init__(author)
        self._behaviors = {
            'GFANAOE': self._from_given_and_last_and_alias_and_affiliation_and_orcid_and_email,
            'GFANA_E': self._from_given_and_last_and_alias_and_affiliation_and_email,
            'GFAN_OE': self._from_given_and_last_and_alias_and_orcid_and_email,
            'GFAN__E': self._from_given_and_last_and_alias_and_email,
            'GFA_AOE': self._from_given_and_last_and_alias_and_affiliation_and_orcid_and_email,
            'GFA_A_E': self._from_given_and_last_and_alias_and_affiliation_and_email,
            'GFA__OE': self._from_given_and_last_and_alias_and_orcid_and_email,
            'GFA___E': self._from_given_and_last_and_alias_and_email,
            'GF_NAOE': self._from_given_and_last_and_affiliation_and_orcid_and_email,
            'GF_NA_E': self._from_given_and_last_and_affiliation_and_email,
            'GF_N_OE': self._from_given_and_last_and_orcid_and_email,
            'GF_N__E': self._from_given_and_last_and_email,
            'GF__AOE': self._from_given_and_last_and_affiliation_and_orcid_and_email,
            'GF__A_E': self._from_given_and_last_and_affiliation_and_email,
            'GF___OE': self._from_given_and_last_and_orcid_and_email,
            'GF____E': self._from_given_and_last_and_email,
            'G_ANAOE': self._from_given_and_alias_and_affiliation_and_orcid_and_email,
            'G_ANA_E': self._from_given_and_alias_and_affiliation_and_email,
            'G_AN_OE': self._from_given_and_alias_and_orcid_and_email,
            'G_AN__E': self._from_given_and_alias_and_email,
            'G_A_AOE': self._from_given_and_alias_and_affiliation_and_orcid_and_email,
            'G_A_A_E': self._from_given_and_alias_and_affiliation_and_email,
            'G_A__OE': self._from_given_and_alias_and_orcid_and_email,
            'G_A___E': self._from_given_and_alias_and_email,
            'G__NAOE': self._from_given_and_affiliation_and_orcid_and_email,
            'G__NA_E': self._from_given_and_affiliation_and_email,
            'G__N_OE': self._from_given_and_orcid_and_email,
            'G__N__E': self._from_given_and_email,
            'G___AOE': self._from_given_and_affiliation_and_orcid_and_email,
            'G___A_E': self._from_given_and_affiliation_and_email,
            'G____OE': self._from_given_and_orcid_and_email,
            'G_____E': self._from_given_and_email,
            '_FANAOE': self._from_last_and_alias_and_affiliation_and_orcid_and_email,
            '_FANA_E': self._from_last_and_alias_and_affiliation_and_email,
            '_FAN_OE': self._from_last_and_alias_and_orcid_and_email,
            '_FAN__E': self._from_last_and_alias_and_email,
            '_FA_AOE': self._from_last_and_alias_and_affiliation_and_orcid_and_email,
            '_FA_A_E': self._from_last_and_alias_and_affiliation_and_email,
            '_FA__OE': self._from_last_and_alias_and_orcid_and_email,
            '_FA___E': self._from_last_and_alias_and_email,
            '_F_NAOE': self._from_last_and_affiliation_and_orcid_and_email,
            '_F_NA_E': self._from_last_and_affiliation_and_email,
            '_F_N_OE': self._from_last_and_orcid_and_email,
            '_F_N__E': self._from_last_and_email,
            '_F__AOE': self._from_last_and_affiliation_and_orcid_and_email,
            '_F__A_E': self._from_last_and_affiliation_and_email,
            '_F___OE': self._from_last_and_orcid_and_email,
            '_F____E': self._from_last_and_email,
            '__ANAOE': self._from_alias_and_name_and_affiliation_and_orcid_and_email,
            '__ANA_E': self._from_alias_and_name_and_affiliation_and_email,
            '__AN_OE': self._from_alias_and_name_and_orcid_and_email,
            '__AN__E': self._from_alias_and_name_and_email,
            '__A_AOE': self._from_alias_and_affiliation_and_orcid_and_email,
            '__A_A_E': self._from_alias_and_affiliation_and_email,
            '__A__OE': self._from_alias_and_orcid_and_email,
            '__A___E': self._from_alias_and_email,
            '___NAOE': self._from_name_and_affiliation_and_orcid_and_email,
            '___NA_E': self._from_name_and_affiliation_and_email,
            '___N_OE': self._from_name_and_orcid_and_email,
            '___N__E': self._from_name_and_email,
            '____AOE': self._from_affiliation_and_orcid_and_email,
            '____A_E': self._from_affiliation_and_email,
            '_____OE': self._from_orcid_and_email,
            '______E': self._from_email,
            'GFANAO_': self._from_given_and_last_and_alias_and_affiliation_and_orcid,
            'GFANA__': self._from_given_and_last_and_alias_and_affiliation,
            'GFAN_O_': self._from_given_and_last_and_alias_and_orcid,
            'GFAN___': self._from_given_and_last_and_alias,
            'GFA_AO_': self._from_given_and_last_and_alias_and_affiliation_and_orcid,
            'GFA_A__': self._from_given_and_last_and_alias_and_affiliation,
            'GFA__O_': self._from_given_and_last_and_alias_and_orcid,
            'GFA____': self._from_given_and_last_and_alias,
            'GF_NAO_': self._from_given_and_last_and_affiliation_and_orcid,
            'GF_NA__': self._from_given_and_last_and_affiliation,
            'GF_N_O_': self._from_given_and_last_and_orcid,
            'GF_N___': self._from_given_and_last,
            'GF__AO_': self._from_given_and_last_and_affiliation_and_orcid,
            'GF__A__': self._from_given_and_last_and_affiliation,
            'GF___O_': self._from_given_and_last_and_orcid,
            'GF_____': self._from_given_and_last,
            'G_ANAO_': self._from_given_and_alias_and_affiliation_and_orcid,
            'G_ANA__': self._from_given_and_alias_and_affiliation,
            'G_AN_O_': self._from_given_and_alias_and_orcid,
            'G_AN___': self._from_given_and_alias,
            'G_A_AO_': self._from_given_and_alias_and_affiliation_and_orcid,
            'G_A_A__': self._from_given_and_alias_and_affiliation,
            'G_A__O_': self._from_given_and_alias_and_orcid,
            'G_A____': self._from_given_and_alias,
            'G__NAO_': self._from_given_and_affiliation_and_orcid,
            'G__NA__': self._from_given_and_affiliation,
            'G__N_O_': self._from_given_and_orcid,
            'G__N___': self._from_given,
            'G___AO_': self._from_given_and_affiliation_and_orcid,
            'G___A__': self._from_given_and_affiliation,
            'G____O_': self._from_given_and_orcid,
            'G______': self._from_given,
            '_FANAO_': self._from_last_and_alias_and_affiliation_and_orcid,
            '_FANA__': self._from_last_and_alias_and_affiliation,
            '_FAN_O_': self._from_last_and_alias_and_orcid,
            '_FAN___': self._from_last_and_alias,
            '_FA_AO_': self._from_last_and_alias_and_affiliation_and_orcid,
            '_FA_A__': self._from_last_and_alias_and_affiliation,
            '_FA__O_': self._from_last_and_alias_and_orcid,
            '_FA____': self._from_last_and_alias,
            '_F_NAO_': self._from_last_and_affiliation_and_orcid,
            '_F_NA__': self._from_last_and_affiliation,
            '_F_N_O_': self._from_last_and_orcid,
            '_F_N___': self._from_last,
            '_F__AO_': self._from_last_and_affiliation_and_orcid,
            '_F__A__': self._from_last_and_affiliation,
            '_F___O_': self._from_last_and_orcid,
            '_F_____': self._from_last,
            '__ANAO_': self._from_alias_and_name_and_affiliation_and_orcid,
            '__ANA__': self._from_alias_and_name_and_affiliation,
            '__AN_O_': self._from_alias_and_name_and_orcid,
            '__AN___': self._from_alias_and_name,
            '__A_AO_': self._from_alias_and_affiliation_and_orcid,
            '__A_A__': self._from_alias_and_affiliation,
            '__A__O_': self._from_alias_and_orcid,
            '__A____': self._from_alias,
            '___NAO_': self._from_name_and_affiliation_and_orcid,
            '___NA__': self._from_name_and_affiliation,
            '___N_O_': self._from_name_and_orcid,
            '___N___': self._from_name,
            '____AO_': self._from_affiliation_and_orcid,
            '____A__': self._from_affiliation,
            '_____O_': self._from_orcid,
            '_______': SchemaorgAuthor._from_thin_air
        }

    def _from_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'email': self._author.get('email')
        }

    def _from_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'email': self._author.get('email')
        }

    def _from_alias_and_email(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'email': self._author.get('email')
        }

    def _from_alias_and_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'email': self._author.get('email')
        }

    def _from_alias_and_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'email': self._author.get('email')
        }

    def _from_alias_and_name_and_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'name': self._author.get('name'),
            'email': self._author.get('email')
        }

    def _from_alias_and_name_and_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'name': self._author.get('name'),
            'email': self._author.get('email')
        }

    def _from_alias_and_name_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'name': self._author.get('name'),
            'email': self._author.get('email')
        }

    def _from_alias_and_name_and_email(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'name': self._author.get('name'),
            'email': self._author.get('email')
        }

    def _from_alias_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'email': self._author.get('email')
        }

    def _from_email(self):
        return {
            '@type': 'Person',
            'email': self._author.get('email')
        }

    def _from_given_and_email(self):
        return {
            '@type': 'Person',
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_alias_and_email(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_alias_and_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_alias_and_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_alias_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_last_and_email(self):
        return {
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_last_and_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_last_and_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_last_and_alias_and_email(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_last_and_alias_and_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_last_and_alias_and_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_last_and_alias_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_last_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_given_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'givenName': self._author.get('given-names'),
            'email': self._author.get('email')
        }

    def _from_last_and_email(self):
        return {
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'email': self._author.get('email')
        }

    def _from_last_and_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'email': self._author.get('email')
        }

    def _from_last_and_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'email': self._author.get('email')
        }

    def _from_last_and_alias_and_email(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'email': self._author.get('email')
        }

    def _from_last_and_alias_and_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'email': self._author.get('email')
        }

    def _from_last_and_alias_and_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'email': self._author.get('email')
        }

    def _from_last_and_alias_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'email': self._author.get('email')
        }

    def _from_last_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'email': self._author.get('email')
        }

    def _from_name_and_email(self):
        return {
            '@type': 'Person',
            'name': self._author.get('name'),
            'email': self._author.get('email')
        }

    def _from_name_and_affiliation_and_email(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'name': self._author.get('name'),
            'email': self._author.get('email')
        }

    def _from_name_and_affiliation_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'name': self._author.get('name'),
            'email': self._author.get('email')
        }

    def _from_name_and_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'name': self._author.get('name'),
            'email': self._author.get('email')
        }

    def _from_orcid_and_email(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'email': self._author.get('email')
        }

    def _from_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            }
        }

    def _from_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            }
        }

    def _from_alias(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias')
        }

    def _from_alias_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
        }

    def _from_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
        }

    def _from_alias_and_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'name': self._author.get('name')
        }

    def _from_alias_and_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'name': self._author.get('name')
        }

    def _from_alias_and_name_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'name': self._author.get('name')
        }

    def _from_alias_and_name(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'name': self._author.get('name')
        }

    def _from_alias_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias')
        }

    def _from_given(self):
        return {
            '@type': 'Person',
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_alias(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_alias_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_alias_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_last(self):
        return {
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_last_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_last_and_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_last_and_alias(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_last_and_alias_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_last_and_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_last_and_alias_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_last_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'familyName': self._get_full_last_name(),
            'givenName': self._author.get('given-names')
        }

    def _from_given_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'givenName': self._author.get('given-names')
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
                'legalName': self._author.get('affiliation')
            },
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_alias(self):
        return {
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_alias_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_alias_and_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_alias_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'alternateName': self._author.get('alias'),
            'familyName': self._get_full_last_name()
        }

    def _from_last_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'familyName': self._get_full_last_name()
        }

    def _from_name(self):
        return {
            '@type': 'Person',
            'name': self._author.get('name')
        }

    def _from_name_and_affiliation(self):
        return {
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'name': self._author.get('name')
        }

    def _from_name_and_affiliation_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'affiliation': {
                '@type': 'Organization',
                'legalName': self._author.get('affiliation')
            },
            'name': self._author.get('name')
        }

    def _from_name_and_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person',
            'name': self._author.get('name')
        }

    def _from_orcid(self):
        return {
            '@id': self._author.get('orcid'),
            '@type': 'Person'
        }

    def as_dict(self):
        key = ''.join([
            self._has_given_name(),
            self._has_family_name(),
            self._has_alias(),
            self._has_name(),
            self._has_affiliation(),
            self._has_orcid(),
            self._has_email()
        ])
        return self._behaviors[key]()
