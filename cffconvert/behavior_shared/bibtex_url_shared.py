from abc import abstractmethod


class BibtexUrlShared:

    def __init__(self, cffobj):
        self._cffobj = cffobj
        self._behaviors = {
            'IRACU': self._from_identifiers_url,
            'IRAC_': self._from_identifiers_url,
            'IRA_U': self._from_identifiers_url,
            'IRA__': self._from_identifiers_url,
            'IR_CU': self._from_identifiers_url,
            'IR_C_': self._from_identifiers_url,
            'IR__U': self._from_identifiers_url,
            'IR___': self._from_identifiers_url,
            'I_ACU': self._from_identifiers_url,
            'I_AC_': self._from_identifiers_url,
            'I_A_U': self._from_identifiers_url,
            'I_A__': self._from_identifiers_url,
            'I__CU': self._from_identifiers_url,
            'I__C_': self._from_identifiers_url,
            'I___U': self._from_identifiers_url,
            'I____': self._from_identifiers_url,
            '_RACU': self._from_url,
            '_RAC_': self._from_repository_code,
            '_RA_U': self._from_url,
            '_RA__': self._from_repository,
            '_R_CU': self._from_url,
            '_R_C_': self._from_repository_code,
            '_R__U': self._from_url,
            '_R___': self._from_repository,
            '__ACU': self._from_url,
            '__AC_': self._from_repository_code,
            '__A_U': self._from_url,
            '__A__': self._from_repository_artifact,
            '___CU': self._from_url,
            '___C_': self._from_repository_code,
            '____U': self._from_url,
            '_____': BibtexUrlShared._from_thin_air
        }

    def _from_identifiers_url(self):
        identifiers = self._cffobj.get('identifiers', list())
        urls = [identifier for identifier in identifiers if identifier.get('type') == 'url']
        if len(urls) > 0:
            return 'url = {' + urls[0].get('value') + '}'
        return None

    def _from_repository(self):
        return 'url = {' + self._cffobj.get('repository') + '}'

    def _from_repository_artifact(self):
        return 'url = {' + self._cffobj.get('repository-artifact') + '}'

    def _from_repository_code(self):
        return 'url = {' + self._cffobj.get('repository-code') + '}'

    @staticmethod
    def _from_thin_air():
        return None

    def _from_url(self):
        return 'url = {' + self._cffobj.get('url') + '}'

    def _has_identifiers_url(self):
        identifiers = self._cffobj.get('identifiers', list())
        urls = [identifier for identifier in identifiers if identifier.get('type') == 'url']
        if len(urls) > 0:
            return 'I'
        return '_'

    def _has_repository(self):
        tmp = self._cffobj.get('repository', None)
        if tmp is not None and tmp != '':
            return 'R'
        return '_'

    def _has_repository_artifact(self):
        tmp = self._cffobj.get('repository-artifact', None)
        if tmp is not None and tmp != '':
            return 'A'
        return '_'

    def _has_repository_code(self):
        tmp = self._cffobj.get('repository-code', None)
        if tmp is not None and tmp != '':
            return 'C'
        return '_'

    def _has_url(self):
        tmp = self._cffobj.get('url', None)
        if tmp is not None and tmp != '':
            return 'U'
        return '_'

    @abstractmethod
    def as_string(self):
        pass
