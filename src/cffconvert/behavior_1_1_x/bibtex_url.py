from cffconvert.behavior_shared.bibtex_url_shared import BibtexUrlShared as Shared


# pylint: disable=too-few-public-methods
class BibtexUrl(Shared):

    def as_string(self):
        key = ''.join([
            self._has_identifiers_url(),
            self._has_repository(),
            self._has_repository_artifact(),
            self._has_repository_code(),
            self._has_url()
        ])
        return self._behaviors[key]()
