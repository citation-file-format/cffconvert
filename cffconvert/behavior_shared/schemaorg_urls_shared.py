from abc import abstractmethod
from cffconvert.behavior_shared.abstract_url_shared import AbstractUrlShared


# pylint: disable=too-few-public-methods
class SchemaorgUrlsShared(AbstractUrlShared):

    def __init__(self, cffobj):
        super().__init__(cffobj)
        self._behaviors = {
            'IRACU': self._from_identifiers_url_and_repository_code,
            'IRAC_': self._from_identifiers_url_and_repository_code,
            'IRA_U': self._from_identifiers_url_and_repository,
            'IRA__': self._from_identifiers_url_and_repository,
            'IR_CU': self._from_identifiers_url_and_repository_code,
            'IR_C_': self._from_identifiers_url_and_repository_code,
            'IR__U': self._from_identifiers_url_and_repository,
            'IR___': self._from_identifiers_url_and_repository,
            'I_ACU': self._from_identifiers_url_and_repository_code,
            'I_AC_': self._from_identifiers_url_and_repository_code,
            'I_A_U': self._from_identifiers_url,
            'I_A__': self._from_identifiers_url,
            'I__CU': self._from_identifiers_url_and_repository_code,
            'I__C_': self._from_identifiers_url_and_repository_code,
            'I___U': self._from_identifiers_url,
            'I____': self._from_identifiers_url,
            '_RACU': self._from_repository_code_and_url,
            '_RAC_': self._from_repository_and_repository_code,
            '_RA_U': self._from_repository_and_url,
            '_RA__': self._from_repository_and_repository_artifact,
            '_R_CU': self._from_repository_code_and_url,
            '_R_C_': self._from_repository_code_and_repository,
            '_R__U': self._from_repository_and_url,
            '_R___': self._from_repository,
            '__ACU': self._from_repository_code_and_url,
            '__AC_': self._from_repository_artifact_and_repository_code,
            '__A_U': self._from_url,
            '__A__': self._from_repository_artifact,
            '___CU': self._from_repository_code_and_url,
            '___C_': self._from_repository_code,
            '____U': self._from_url,
            '_____': SchemaorgUrlsShared._from_thin_air
        }

    def _from_identifiers_url_and_repository_code(self):
        return self._cffobj.get('repository-code'), self._get_urls_from_identifiers()[0].get('value')

    def _from_identifiers_url_and_repository(self):
        return self._cffobj.get('repository'), self._get_urls_from_identifiers()[0].get('value')

    def _from_identifiers_url(self):
        return None, self._get_urls_from_identifiers()[0].get('value')

    def _from_repository_and_repository_artifact(self):
        return self._cffobj.get('repository'), self._cffobj.get('repository-artifact')

    def _from_repository_and_repository_code(self):
        return self._cffobj.get('repository-code'), self._cffobj.get('repository')

    def _from_repository_and_url(self):
        return self._cffobj.get('repository'), self._cffobj.get('url')

    def _from_repository_artifact_and_repository_code(self):
        return self._cffobj.get('repository-code'), self._cffobj.get('repository-artifact')

    def _from_repository_artifact(self):
        return None, self._cffobj.get('repository-artifact')

    def _from_repository_code_and_repository(self):
        return self._cffobj.get('repository-code'), self._cffobj.get('repository')

    def _from_repository_code_and_url(self):
        return self._cffobj.get('repository-code'), self._cffobj.get('url')

    def _from_repository_code(self):
        return self._cffobj.get('repository-code'), self._cffobj.get('repository-code')

    def _from_repository(self):
        return self._cffobj.get('repository'), self._cffobj.get('repository')

    @staticmethod
    def _from_thin_air():
        return None, None

    def _from_url(self):
        return None, self._cffobj.get('url')

    @abstractmethod
    def as_tuple(self):
        pass
