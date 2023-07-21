from cffconvert.lib.cff_1_x_x.authors.base import BaseAuthor


# pylint: disable=too-few-public-methods
class ApalikeAuthor(BaseAuthor):

    def __init__(self, author):
        super().__init__(author)
        self._behaviors = {
            "GFANAOE": self._from_given_and_last,
            "GFANAO_": self._from_given_and_last,
            "GFANA_E": self._from_given_and_last,
            "GFANA__": self._from_given_and_last,
            "GFAN_OE": self._from_given_and_last,
            "GFAN_O_": self._from_given_and_last,
            "GFAN__E": self._from_given_and_last,
            "GFAN___": self._from_given_and_last,
            "GFA_AOE": self._from_given_and_last,
            "GFA_AO_": self._from_given_and_last,
            "GFA_A_E": self._from_given_and_last,
            "GFA_A__": self._from_given_and_last,
            "GFA__OE": self._from_given_and_last,
            "GFA__O_": self._from_given_and_last,
            "GFA___E": self._from_given_and_last,
            "GFA____": self._from_given_and_last,
            "GF_NAOE": self._from_given_and_last,
            "GF_NAO_": self._from_given_and_last,
            "GF_NA_E": self._from_given_and_last,
            "GF_NA__": self._from_given_and_last,
            "GF_N_OE": self._from_given_and_last,
            "GF_N_O_": self._from_given_and_last,
            "GF_N__E": self._from_given_and_last,
            "GF_N___": self._from_given_and_last,
            "GF__AOE": self._from_given_and_last,
            "GF__AO_": self._from_given_and_last,
            "GF__A_E": self._from_given_and_last,
            "GF__A__": self._from_given_and_last,
            "GF___OE": self._from_given_and_last,
            "GF___O_": self._from_given_and_last,
            "GF____E": self._from_given_and_last,
            "GF_____": self._from_given_and_last,
            "G_ANAOE": self._from_given,
            "G_ANAO_": self._from_given,
            "G_ANA_E": self._from_given,
            "G_ANA__": self._from_given,
            "G_AN_OE": self._from_given,
            "G_AN_O_": self._from_given,
            "G_AN__E": self._from_given,
            "G_AN___": self._from_given,
            "G_A_AOE": self._from_given,
            "G_A_AO_": self._from_given,
            "G_A_A_E": self._from_given,
            "G_A_A__": self._from_given,
            "G_A__OE": self._from_given,
            "G_A__O_": self._from_given,
            "G_A___E": self._from_given,
            "G_A____": self._from_given,
            "G__NAOE": self._from_given,
            "G__NAO_": self._from_given,
            "G__NA_E": self._from_given,
            "G__NA__": self._from_given,
            "G__N_OE": self._from_given,
            "G__N_O_": self._from_given,
            "G__N__E": self._from_given,
            "G__N___": self._from_given,
            "G___AOE": self._from_given,
            "G___AO_": self._from_given,
            "G___A_E": self._from_given,
            "G___A__": self._from_given,
            "G____OE": self._from_given,
            "G____O_": self._from_given,
            "G_____E": self._from_given,
            "G______": self._from_given,
            "_FANAOE": self._from_last,
            "_FANAO_": self._from_last,
            "_FANA_E": self._from_last,
            "_FANA__": self._from_last,
            "_FAN_OE": self._from_last,
            "_FAN_O_": self._from_last,
            "_FAN__E": self._from_last,
            "_FAN___": self._from_last,
            "_FA_AOE": self._from_last,
            "_FA_AO_": self._from_last,
            "_FA_A_E": self._from_last,
            "_FA_A__": self._from_last,
            "_FA__OE": self._from_last,
            "_FA__O_": self._from_last,
            "_FA___E": self._from_last,
            "_FA____": self._from_last,
            "_F_NAOE": self._from_last,
            "_F_NAO_": self._from_last,
            "_F_NA_E": self._from_last,
            "_F_NA__": self._from_last,
            "_F_N_OE": self._from_last,
            "_F_N_O_": self._from_last,
            "_F_N__E": self._from_last,
            "_F_N___": self._from_last,
            "_F__AOE": self._from_last,
            "_F__AO_": self._from_last,
            "_F__A_E": self._from_last,
            "_F__A__": self._from_last,
            "_F___OE": self._from_last,
            "_F___O_": self._from_last,
            "_F____E": self._from_last,
            "_F_____": self._from_last,
            "__ANAOE": self._from_name,
            "__ANAO_": self._from_name,
            "__ANA_E": self._from_name,
            "__ANA__": self._from_name,
            "__AN_OE": self._from_name,
            "__AN_O_": self._from_name,
            "__AN__E": self._from_name,
            "__AN___": self._from_name,
            "__A_AOE": self._from_alias,
            "__A_AO_": self._from_alias,
            "__A_A_E": self._from_alias,
            "__A_A__": self._from_alias,
            "__A__OE": self._from_alias,
            "__A__O_": self._from_alias,
            "__A___E": self._from_alias,
            "__A____": self._from_alias,
            "___NAOE": self._from_name,
            "___NAO_": self._from_name,
            "___NA_E": self._from_name,
            "___NA__": self._from_name,
            "___N_OE": self._from_name,
            "___N_O_": self._from_name,
            "___N__E": self._from_name,
            "___N___": self._from_name,
            "____AOE": ApalikeAuthor._from_thin_air,
            "____AO_": ApalikeAuthor._from_thin_air,
            "____A_E": ApalikeAuthor._from_thin_air,
            "____A__": ApalikeAuthor._from_thin_air,
            "_____OE": ApalikeAuthor._from_thin_air,
            "_____O_": ApalikeAuthor._from_thin_air,
            "______E": ApalikeAuthor._from_thin_air,
            "_______": ApalikeAuthor._from_thin_air
        }

    def _from_alias(self):
        return self._author.get("alias")

    def _from_given_and_last(self):
        return self._get_full_last_name() + " " + self._get_initials()

    def _from_given(self):
        return self._author.get("given-names")

    def _from_last(self):
        return self._get_full_last_name()

    def _from_name(self):
        return self._author.get("name")

    def _get_initials(self):
        given_names = self._author.get("given-names").split(" ")
        return "".join([given_name[0] + "." for given_name in given_names])

    def as_string(self):
        key = self._get_key()
        return self._behaviors[key]()
