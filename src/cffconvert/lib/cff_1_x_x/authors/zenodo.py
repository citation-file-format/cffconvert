from cffconvert.lib.cff_1_x_x.authors.base import BaseAuthor


# pylint: disable=too-few-public-methods
class ZenodoAuthor(BaseAuthor):

    def __init__(self, author):
        super().__init__(author)
        self._behaviors = {
            "GFANAOE": self._from_given_and_last_and_affiliation_and_orcid,
            "GFANAO_": self._from_given_and_last_and_affiliation_and_orcid,
            "GFANA_E": self._from_given_and_last_and_affiliation,
            "GFANA__": self._from_given_and_last_and_affiliation,
            "GFAN_OE": self._from_given_and_last_and_orcid,
            "GFAN_O_": self._from_given_and_last_and_orcid,
            "GFAN__E": self._from_given_and_last,
            "GFAN___": self._from_given_and_last,
            "GFA_AOE": self._from_given_and_last_and_affiliation_and_orcid,
            "GFA_AO_": self._from_given_and_last_and_affiliation_and_orcid,
            "GFA_A_E": self._from_given_and_last_and_affiliation,
            "GFA_A__": self._from_given_and_last_and_affiliation,
            "GFA__OE": self._from_given_and_last_and_orcid,
            "GFA__O_": self._from_given_and_last_and_orcid,
            "GFA___E": self._from_given_and_last,
            "GFA____": self._from_given_and_last,
            "GF_NAOE": self._from_given_and_last_and_affiliation_and_orcid,
            "GF_NAO_": self._from_given_and_last_and_affiliation_and_orcid,
            "GF_NA_E": self._from_given_and_last_and_affiliation,
            "GF_NA__": self._from_given_and_last_and_affiliation,
            "GF_N_OE": self._from_given_and_last_and_orcid,
            "GF_N_O_": self._from_given_and_last_and_orcid,
            "GF_N__E": self._from_given_and_last,
            "GF_N___": self._from_given_and_last,
            "GF__AOE": self._from_given_and_last_and_affiliation_and_orcid,
            "GF__AO_": self._from_given_and_last_and_affiliation_and_orcid,
            "GF__A_E": self._from_given_and_last_and_affiliation,
            "GF__A__": self._from_given_and_last_and_affiliation,
            "GF___OE": self._from_given_and_last_and_orcid,
            "GF___O_": self._from_given_and_last_and_orcid,
            "GF____E": self._from_given_and_last,
            "GF_____": self._from_given_and_last,
            "G_ANAOE": self._from_given_and_affiliation_and_orcid,
            "G_ANAO_": self._from_given_and_affiliation_and_orcid,
            "G_ANA_E": self._from_given_and_affiliation,
            "G_ANA__": self._from_given_and_affiliation,
            "G_AN_OE": self._from_given_and_orcid,
            "G_AN_O_": self._from_given_and_orcid,
            "G_AN__E": self._from_given,
            "G_AN___": self._from_given,
            "G_A_AOE": self._from_given_and_affiliation_and_orcid,
            "G_A_AO_": self._from_given_and_affiliation_and_orcid,
            "G_A_A_E": self._from_given_and_affiliation,
            "G_A_A__": self._from_given_and_affiliation,
            "G_A__OE": self._from_given_and_orcid,
            "G_A__O_": self._from_given_and_orcid,
            "G_A___E": self._from_given,
            "G_A____": self._from_given,
            "G__NAOE": self._from_given_and_affiliation_and_orcid,
            "G__NAO_": self._from_given_and_affiliation_and_orcid,
            "G__NA_E": self._from_given_and_affiliation,
            "G__NA__": self._from_given_and_affiliation,
            "G__N_OE": self._from_given_and_orcid,
            "G__N_O_": self._from_given_and_orcid,
            "G__N__E": self._from_given,
            "G__N___": self._from_given,
            "G___AOE": self._from_given_and_affiliation_and_orcid,
            "G___AO_": self._from_given_and_affiliation_and_orcid,
            "G___A_E": self._from_given_and_affiliation,
            "G___A__": self._from_given_and_affiliation,
            "G____OE": self._from_given_and_orcid,
            "G____O_": self._from_given_and_orcid,
            "G_____E": self._from_given,
            "G______": self._from_given,
            "_FANAOE": self._from_last_and_affiliation_and_orcid,
            "_FANAO_": self._from_last_and_affiliation_and_orcid,
            "_FANA_E": self._from_last_and_affiliation,
            "_FANA__": self._from_last_and_affiliation,
            "_FAN_OE": self._from_last_and_orcid,
            "_FAN_O_": self._from_last_and_orcid,
            "_FAN__E": self._from_last,
            "_FAN___": self._from_last,
            "_FA_AOE": self._from_last_and_affiliation_and_orcid,
            "_FA_AO_": self._from_last_and_affiliation_and_orcid,
            "_FA_A_E": self._from_last_and_affiliation,
            "_FA_A__": self._from_last_and_affiliation,
            "_FA__OE": self._from_last_and_orcid,
            "_FA__O_": self._from_last_and_orcid,
            "_FA___E": self._from_last,
            "_FA____": self._from_last,
            "_F_NAOE": self._from_last_and_affiliation_and_orcid,
            "_F_NAO_": self._from_last_and_affiliation_and_orcid,
            "_F_NA_E": self._from_last_and_affiliation,
            "_F_NA__": self._from_last_and_affiliation,
            "_F_N_OE": self._from_last_and_orcid,
            "_F_N_O_": self._from_last_and_orcid,
            "_F_N__E": self._from_last,
            "_F_N___": self._from_last,
            "_F__AOE": self._from_last_and_affiliation_and_orcid,
            "_F__AO_": self._from_last_and_affiliation_and_orcid,
            "_F__A_E": self._from_last_and_affiliation,
            "_F__A__": self._from_last_and_affiliation,
            "_F___OE": self._from_last_and_orcid,
            "_F___O_": self._from_last_and_orcid,
            "_F____E": self._from_last,
            "_F_____": self._from_last,
            "__ANAOE": self._from_name_and_affiliation_and_orcid,
            "__ANAO_": self._from_name_and_affiliation_and_orcid,
            "__ANA_E": self._from_name_and_affiliation,
            "__ANA__": self._from_name_and_affiliation,
            "__AN_OE": self._from_name_and_orcid,
            "__AN_O_": self._from_name_and_orcid,
            "__AN__E": self._from_name,
            "__AN___": self._from_name,
            "__A_AOE": self._from_alias_and_affiliation_and_orcid,
            "__A_AO_": self._from_alias_and_affiliation_and_orcid,
            "__A_A_E": self._from_alias_and_affiliation,
            "__A_A__": self._from_alias_and_affiliation,
            "__A__OE": self._from_alias_and_orcid,
            "__A__O_": self._from_alias_and_orcid,
            "__A___E": self._from_alias,
            "__A____": self._from_alias,
            "___NAOE": self._from_name_and_affiliation_and_orcid,
            "___NAO_": self._from_name_and_affiliation_and_orcid,
            "___NA_E": self._from_name_and_affiliation,
            "___NA__": self._from_name_and_affiliation,
            "___N_OE": self._from_name_and_orcid,
            "___N_O_": self._from_name_and_orcid,
            "___N__E": self._from_name,
            "___N___": self._from_name,
            "____AOE": self._from_affiliation_and_orcid,
            "____AO_": self._from_affiliation_and_orcid,
            "____A_E": self._from_affiliation,
            "____A__": self._from_affiliation,
            "_____OE": self._from_orcid,
            "_____O_": self._from_orcid,
            "______E": ZenodoAuthor._from_thin_air,
            "_______": ZenodoAuthor._from_thin_air
        }

    def _from_affiliation(self):
        return {
            "affiliation": self._author.get("affiliation")
        }

    def _from_affiliation_and_orcid(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_alias(self):
        return {
            "name": self._author.get("alias")
        }

    def _from_alias_and_affiliation(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._author.get("alias")
        }

    def _from_alias_and_affiliation_and_orcid(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._author.get("alias"),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_alias_and_orcid(self):
        return {
            "name": self._author.get("alias"),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_given(self):
        return {
            "name": self._author.get("given-names")
        }

    def _from_given_and_affiliation(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._author.get("given-names")
        }

    def _from_given_and_affiliation_and_orcid(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._author.get("given-names"),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_given_and_last(self):
        return {
            "name": self._get_full_last_name() + ", " + self._author.get("given-names")
        }

    def _from_given_and_last_and_affiliation(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._get_full_last_name() + ", " + self._author.get("given-names")
        }

    def _from_given_and_last_and_affiliation_and_orcid(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._get_full_last_name() + ", " + self._author.get("given-names"),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_given_and_last_and_orcid(self):
        return {
            "name": self._get_full_last_name() + ", " + self._author.get("given-names"),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_given_and_orcid(self):
        return {
            "name": self._author.get("given-names"),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_last(self):
        return {
            "name": self._get_full_last_name()
        }

    def _from_last_and_affiliation(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._get_full_last_name()
        }

    def _from_last_and_affiliation_and_orcid(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._get_full_last_name(),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_last_and_orcid(self):
        return {
            "name": self._get_full_last_name(),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_name(self):
        return {
            "name": self._author.get("name")
        }

    def _from_name_and_affiliation(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._author.get("name")
        }

    def _from_name_and_affiliation_and_orcid(self):
        return {
            "affiliation": self._author.get("affiliation"),
            "name": self._author.get("name"),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_name_and_orcid(self):
        return {
            "name": self._author.get("name"),
            "orcid": self._get_id_from_orcid_url()
        }

    def _from_orcid(self):
        return {
            "orcid": self._get_id_from_orcid_url()
        }

    def _get_id_from_orcid_url(self):
        return self._author.get("orcid").replace("https://orcid.org/", "")

    def as_dict(self):
        key = self._get_key()
        return self._behaviors[key]()
