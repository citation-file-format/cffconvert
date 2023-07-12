from cffconvert.behavior_shared.endnote_url_shared import EndnoteUrlShared as Shared


# pylint: disable=too-few-public-methods
class EndnoteUrl(Shared):

    def as_string(self):
        key = ''.join([
            self._has_identifiers_url(),
            self._has_repository(),
            self._has_repository_artifact(),
            self._has_repository_code(),
            self._has_url()
        ])
        return self._behaviors[key]()
