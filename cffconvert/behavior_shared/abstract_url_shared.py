from abc import ABC


# pylint: disable=too-few-public-methods
class AbstractUrlShared(ABC):

    def __init__(self, cffobj):
        self._cffobj = cffobj
        self._behaviors = None

    def _get_urls_from_identifiers(self):
        identifiers = self._cffobj.get('identifiers', [])
        return [identifier for identifier in identifiers if identifier.get('type') == 'url']

    def _has_identifiers_url(self):
        urls = self._get_urls_from_identifiers()
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
