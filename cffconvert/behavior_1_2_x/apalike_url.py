from cffconvert.behavior_shared.apalike_url_shared import ApalikeUrlShared as Shared


class ApalikeUrl(Shared):

    def __init__(self, cffobj):
        super().__init__(cffobj)

    def as_string(self):
        state = [
            ('I', self._has_identifiers_url()),
            ('R', self._has_repository()),
            ('A', self._has_repository_artifact()),
            ('C', self._has_repository_code()),
            ('U', self._has_url())
        ]
        key = ''.join([item[0] if item[1] is True else '_' for item in state])
        return self._behaviors[key]()
