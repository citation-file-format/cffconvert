from cffconvert.lib.cff_1_x_x.urls.base import BaseUrl


# pylint: disable=too-few-public-methods
class BiblatexUrl(BaseUrl):

    def __init__(self, cffobj):
        super().__init__(cffobj)
        self._behaviors = {
            "IRACU": self._from_identifiers_url,
            "IRAC_": self._from_identifiers_url,
            "IRA_U": self._from_identifiers_url,
            "IRA__": self._from_identifiers_url,
            "IR_CU": self._from_identifiers_url,
            "IR_C_": self._from_identifiers_url,
            "IR__U": self._from_identifiers_url,
            "IR___": self._from_identifiers_url,
            "I_ACU": self._from_identifiers_url,
            "I_AC_": self._from_identifiers_url,
            "I_A_U": self._from_identifiers_url,
            "I_A__": self._from_identifiers_url,
            "I__CU": self._from_identifiers_url,
            "I__C_": self._from_identifiers_url,
            "I___U": self._from_identifiers_url,
            "I____": self._from_identifiers_url,
            "_RACU": self._from_url,
            "_RAC_": self._from_repository_code,
            "_RA_U": self._from_url,
            "_RA__": self._from_repository,
            "_R_CU": self._from_url,
            "_R_C_": self._from_repository_code,
            "_R__U": self._from_url,
            "_R___": self._from_repository,
            "__ACU": self._from_url,
            "__AC_": self._from_repository_code,
            "__A_U": self._from_url,
            "__A__": self._from_repository_artifact,
            "___CU": self._from_url,
            "___C_": self._from_repository_code,
            "____U": self._from_url,
            "_____": BiblatexUrl._from_thin_air
        }

    def _from_identifiers_url(self):
        urls = self._get_urls_from_identifiers()
        if len(urls) > 0:
            return f"url = { '{' + urls[0].get('value') + '}' }"
        return None

    def _from_repository(self):
        return f"url = { '{' + self._cffobj.get('repository') + '}' }"

    def _from_repository_artifact(self):
        return f"url = { '{' + self._cffobj.get('repository-artifact') + '}' }"

    def _from_repository_code(self):
        return f"url = { '{' + self._cffobj.get('repository-code') + '}' }"

    @staticmethod
    def _from_thin_air():
        return None

    def _from_url(self):
        return f"url = { '{' + self._cffobj.get('url') + '}' }"

    def as_string(self):
        key = "".join([
            self._has_identifiers_url(),
            self._has_repository(),
            self._has_repository_artifact(),
            self._has_repository_code(),
            self._has_url()
        ])
        return self._behaviors[key]()
