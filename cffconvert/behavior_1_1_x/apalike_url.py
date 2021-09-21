from cffconvert.behavior_shared.apalike_url_shared import ApalikeUrlShared as Shared


class ApalikeUrl(Shared):

    def __init__(self, cffobj):
        super().__init__(cffobj)

    def as_string(self):
        key = ''.join([
            self._has_identifiers_url(),
            self._has_repository(),
            self._has_repository_artifact(),
            self._has_repository_code(),
            self._has_url()
        ])
        return self._behaviors[key]()
