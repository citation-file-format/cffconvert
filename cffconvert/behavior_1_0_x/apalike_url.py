from cffconvert.behavior_shared.apalike_url_shared import ApalikeUrlShared as Shared


# pylint: disable=too-few-public-methods
class ApalikeUrl(Shared):

    def as_string(self):
        key = ''.join([
            '_',
            self._has_repository(),
            self._has_repository_artifact(),
            self._has_repository_code(),
            self._has_url()
        ])
        return self._behaviors[key]()
