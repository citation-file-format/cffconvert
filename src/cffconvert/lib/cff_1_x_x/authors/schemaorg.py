from cffconvert.lib.cff_1_x_x.authors.base import BaseAuthor


# pylint: disable=too-few-public-methods
class SchemaorgAuthor(BaseAuthor):

    def __init__(self, author):
        super().__init__(author)
        self._behaviors = {
            "GFANAOE": self._from_given_and_last_and_alias_and_affiliation_and_orcid_and_email,
            "GFANAO_": self._from_given_and_last_and_alias_and_affiliation_and_orcid,
            "GFANA_E": self._from_given_and_last_and_alias_and_affiliation_and_email,
            "GFANA__": self._from_given_and_last_and_alias_and_affiliation,
            "GFAN_OE": self._from_given_and_last_and_alias_and_orcid_and_email,
            "GFAN_O_": self._from_given_and_last_and_alias_and_orcid,
            "GFAN__E": self._from_given_and_last_and_alias_and_email,
            "GFAN___": self._from_given_and_last_and_alias,
            "GFA_AOE": self._from_given_and_last_and_alias_and_affiliation_and_orcid_and_email,
            "GFA_AO_": self._from_given_and_last_and_alias_and_affiliation_and_orcid,
            "GFA_A_E": self._from_given_and_last_and_alias_and_affiliation_and_email,
            "GFA_A__": self._from_given_and_last_and_alias_and_affiliation,
            "GFA__OE": self._from_given_and_last_and_alias_and_orcid_and_email,
            "GFA__O_": self._from_given_and_last_and_alias_and_orcid,
            "GFA___E": self._from_given_and_last_and_alias_and_email,
            "GFA____": self._from_given_and_last_and_alias,
            "GF_NAOE": self._from_given_and_last_and_affiliation_and_orcid_and_email,
            "GF_NAO_": self._from_given_and_last_and_affiliation_and_orcid,
            "GF_NA_E": self._from_given_and_last_and_affiliation_and_email,
            "GF_NA__": self._from_given_and_last_and_affiliation,
            "GF_N_OE": self._from_given_and_last_and_orcid_and_email,
            "GF_N_O_": self._from_given_and_last_and_orcid,
            "GF_N__E": self._from_given_and_last_and_email,
            "GF_N___": self._from_given_and_last,
            "GF__AOE": self._from_given_and_last_and_affiliation_and_orcid_and_email,
            "GF__AO_": self._from_given_and_last_and_affiliation_and_orcid,
            "GF__A_E": self._from_given_and_last_and_affiliation_and_email,
            "GF__A__": self._from_given_and_last_and_affiliation,
            "GF___OE": self._from_given_and_last_and_orcid_and_email,
            "GF___O_": self._from_given_and_last_and_orcid,
            "GF____E": self._from_given_and_last_and_email,
            "GF_____": self._from_given_and_last,
            "G_ANAOE": self._from_given_and_alias_and_affiliation_and_orcid_and_email,
            "G_ANAO_": self._from_given_and_alias_and_affiliation_and_orcid,
            "G_ANA_E": self._from_given_and_alias_and_affiliation_and_email,
            "G_ANA__": self._from_given_and_alias_and_affiliation,
            "G_AN_OE": self._from_given_and_alias_and_orcid_and_email,
            "G_AN_O_": self._from_given_and_alias_and_orcid,
            "G_AN__E": self._from_given_and_alias_and_email,
            "G_AN___": self._from_given_and_alias,
            "G_A_AOE": self._from_given_and_alias_and_affiliation_and_orcid_and_email,
            "G_A_AO_": self._from_given_and_alias_and_affiliation_and_orcid,
            "G_A_A_E": self._from_given_and_alias_and_affiliation_and_email,
            "G_A_A__": self._from_given_and_alias_and_affiliation,
            "G_A__OE": self._from_given_and_alias_and_orcid_and_email,
            "G_A__O_": self._from_given_and_alias_and_orcid,
            "G_A___E": self._from_given_and_alias_and_email,
            "G_A____": self._from_given_and_alias,
            "G__NAOE": self._from_given_and_affiliation_and_orcid_and_email,
            "G__NAO_": self._from_given_and_affiliation_and_orcid,
            "G__NA_E": self._from_given_and_affiliation_and_email,
            "G__NA__": self._from_given_and_affiliation,
            "G__N_OE": self._from_given_and_orcid_and_email,
            "G__N_O_": self._from_given_and_orcid,
            "G__N__E": self._from_given_and_email,
            "G__N___": self._from_given,
            "G___AOE": self._from_given_and_affiliation_and_orcid_and_email,
            "G___AO_": self._from_given_and_affiliation_and_orcid,
            "G___A_E": self._from_given_and_affiliation_and_email,
            "G___A__": self._from_given_and_affiliation,
            "G____OE": self._from_given_and_orcid_and_email,
            "G____O_": self._from_given_and_orcid,
            "G_____E": self._from_given_and_email,
            "G______": self._from_given,
            "_FANAOE": self._from_last_and_alias_and_affiliation_and_orcid_and_email,
            "_FANAO_": self._from_last_and_alias_and_affiliation_and_orcid,
            "_FANA_E": self._from_last_and_alias_and_affiliation_and_email,
            "_FANA__": self._from_last_and_alias_and_affiliation,
            "_FAN_OE": self._from_last_and_alias_and_orcid_and_email,
            "_FAN_O_": self._from_last_and_alias_and_orcid,
            "_FAN__E": self._from_last_and_alias_and_email,
            "_FAN___": self._from_last_and_alias,
            "_FA_AOE": self._from_last_and_alias_and_affiliation_and_orcid_and_email,
            "_FA_AO_": self._from_last_and_alias_and_affiliation_and_orcid,
            "_FA_A_E": self._from_last_and_alias_and_affiliation_and_email,
            "_FA_A__": self._from_last_and_alias_and_affiliation,
            "_FA__OE": self._from_last_and_alias_and_orcid_and_email,
            "_FA__O_": self._from_last_and_alias_and_orcid,
            "_FA___E": self._from_last_and_alias_and_email,
            "_FA____": self._from_last_and_alias,
            "_F_NAOE": self._from_last_and_affiliation_and_orcid_and_email,
            "_F_NAO_": self._from_last_and_affiliation_and_orcid,
            "_F_NA_E": self._from_last_and_affiliation_and_email,
            "_F_NA__": self._from_last_and_affiliation,
            "_F_N_OE": self._from_last_and_orcid_and_email,
            "_F_N_O_": self._from_last_and_orcid,
            "_F_N__E": self._from_last_and_email,
            "_F_N___": self._from_last,
            "_F__AOE": self._from_last_and_affiliation_and_orcid_and_email,
            "_F__AO_": self._from_last_and_affiliation_and_orcid,
            "_F__A_E": self._from_last_and_affiliation_and_email,
            "_F__A__": self._from_last_and_affiliation,
            "_F___OE": self._from_last_and_orcid_and_email,
            "_F___O_": self._from_last_and_orcid,
            "_F____E": self._from_last_and_email,
            "_F_____": self._from_last,
            "__ANAOE": self._from_alias_and_name_and_orcid_and_email,
            "__ANAO_": self._from_alias_and_name_and_orcid,
            "__ANA_E": self._from_alias_and_name_and_email,
            "__ANA__": self._from_alias_and_name,
            "__AN_OE": self._from_alias_and_name_and_orcid_and_email,
            "__AN_O_": self._from_alias_and_name_and_orcid,
            "__AN__E": self._from_alias_and_name_and_email,
            "__AN___": self._from_alias_and_name,
            "__A_AOE": self._from_alias_and_affiliation_and_orcid_and_email,
            "__A_AO_": self._from_alias_and_affiliation_and_orcid,
            "__A_A_E": self._from_alias_and_affiliation_and_email,
            "__A_A__": self._from_alias_and_affiliation,
            "__A__OE": self._from_alias_and_orcid_and_email,
            "__A__O_": self._from_alias_and_orcid,
            "__A___E": self._from_alias_and_email,
            "__A____": self._from_alias,
            "___NAOE": self._from_name_and_orcid_and_email,
            "___NAO_": self._from_name_and_orcid,
            "___NA_E": self._from_name_and_email,
            "___NA__": self._from_name,
            "___N_OE": self._from_name_and_orcid_and_email,
            "___N_O_": self._from_name_and_orcid,
            "___N__E": self._from_name_and_email,
            "___N___": self._from_name,
            "____AOE": self._from_affiliation_and_orcid_and_email,
            "____AO_": self._from_affiliation_and_orcid,
            "____A_E": self._from_affiliation_and_email,
            "____A__": self._from_affiliation,
            "_____OE": self._from_orcid_and_email,
            "_____O_": self._from_orcid,
            "______E": self._from_email,
            "_______": SchemaorgAuthor._from_thin_air
        }

    def _from_affiliation_and_email(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "email": self._author.get("email")
        }

    def _from_affiliation_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "email": self._author.get("email")
        }

    def _from_alias_and_email(self):
        return {
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "email": self._author.get("email")
        }

    def _from_alias_and_affiliation_and_email(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "email": self._author.get("email")
        }

    def _from_alias_and_affiliation_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "email": self._author.get("email")
        }

    def _from_alias_and_name_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Organization",
            "alternateName": self._author.get("alias"),
            "name": self._author.get("name"),
            "email": self._author.get("email")
        }

    def _from_alias_and_name_and_email(self):
        return {
            "@type": "Organization",
            "alternateName": self._author.get("alias"),
            "name": self._author.get("name"),
            "email": self._author.get("email")
        }

    def _from_alias_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "email": self._author.get("email")
        }

    def _from_email(self):
        return {
            "@type": "Person",
            "email": self._author.get("email")
        }

    def _from_given_and_email(self):
        return {
            "@type": "Person",
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_affiliation_and_email(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_affiliation_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_alias_and_email(self):
        return {
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_alias_and_affiliation_and_email(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_alias_and_affiliation_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_alias_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_last_and_email(self):
        return {
            "@type": "Person",
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_last_and_affiliation_and_email(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_last_and_affiliation_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_last_and_alias_and_email(self):
        return {
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_last_and_alias_and_affiliation_and_email(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_last_and_alias_and_affiliation_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_last_and_alias_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_last_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_given_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "givenName": self._author.get("given-names"),
            "email": self._author.get("email")
        }

    def _from_last_and_email(self):
        return {
            "@type": "Person",
            "familyName": self._get_full_last_name(),
            "email": self._author.get("email")
        }

    def _from_last_and_affiliation_and_email(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "familyName": self._get_full_last_name(),
            "email": self._author.get("email")
        }

    def _from_last_and_affiliation_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "familyName": self._get_full_last_name(),
            "email": self._author.get("email")
        }

    def _from_last_and_alias_and_email(self):
        return {
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "email": self._author.get("email")
        }

    def _from_last_and_alias_and_affiliation_and_email(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "email": self._author.get("email")
        }

    def _from_last_and_alias_and_affiliation_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "email": self._author.get("email")
        }

    def _from_last_and_alias_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "email": self._author.get("email")
        }

    def _from_last_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "familyName": self._get_full_last_name(),
            "email": self._author.get("email")
        }

    def _from_name_and_email(self):
        return {
            "@type": "Organization",
            "name": self._author.get("name"),
            "email": self._author.get("email")
        }

    def _from_name_and_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Organization",
            "name": self._author.get("name"),
            "email": self._author.get("email")
        }

    def _from_orcid_and_email(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "email": self._author.get("email")
        }

    def _from_affiliation(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            }
        }

    def _from_affiliation_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            }
        }

    def _from_alias(self):
        return {
            "@type": "Person",
            "alternateName": self._author.get("alias")
        }

    def _from_alias_and_affiliation(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
        }

    def _from_alias_and_affiliation_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
        }

    def _from_alias_and_name_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Organization",
            "alternateName": self._author.get("alias"),
            "name": self._author.get("name")
        }

    def _from_alias_and_name(self):
        return {
            "@type": "Organization",
            "alternateName": self._author.get("alias"),
            "name": self._author.get("name")
        }

    def _from_alias_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "alternateName": self._author.get("alias")
        }

    def _from_given(self):
        return {
            "@type": "Person",
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_affiliation(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_affiliation_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_alias(self):
        return {
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_alias_and_affiliation(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_alias_and_affiliation_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_alias_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_last(self):
        return {
            "@type": "Person",
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_last_and_affiliation(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_last_and_affiliation_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_last_and_alias(self):
        return {
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_last_and_alias_and_affiliation(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_last_and_alias_and_affiliation_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_last_and_alias_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_last_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "familyName": self._get_full_last_name(),
            "givenName": self._author.get("given-names")
        }

    def _from_given_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "givenName": self._author.get("given-names")
        }

    def _from_last(self):
        return {
            "@type": "Person",
            "familyName": self._get_full_last_name()
        }

    def _from_last_and_affiliation(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "familyName": self._get_full_last_name()
        }

    def _from_last_and_affiliation_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "familyName": self._get_full_last_name()
        }

    def _from_last_and_alias(self):
        return {
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name()
        }

    def _from_last_and_alias_and_affiliation(self):
        return {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name()
        }

    def _from_last_and_alias_and_affiliation_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": self._author.get("affiliation")
            },
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name()
        }

    def _from_last_and_alias_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "alternateName": self._author.get("alias"),
            "familyName": self._get_full_last_name()
        }

    def _from_last_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person",
            "familyName": self._get_full_last_name()
        }

    def _from_name(self):
        return {
            "@type": "Organization",
            "name": self._author.get("name")
        }

    def _from_name_and_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Organization",
            "name": self._author.get("name")
        }

    def _from_orcid(self):
        return {
            "@id": self._author.get("orcid"),
            "@type": "Person"
        }

    def as_dict(self):
        key = self._get_key()
        return self._behaviors[key]()
