from cffconvert.behavior_shared.endnote_url_shared import EndnoteUrlShared as Shared


class EndnoteUrl(Shared):

    def __init__(self, cffobj):
        super().__init__(cffobj)

    def as_string(self):
        key = ''.join([
            '_',
            self._has_repository(),
            self._has_repository_artifact(),
            self._has_repository_code(),
            self._has_url()
        ])
        return self._behaviors[key]()
