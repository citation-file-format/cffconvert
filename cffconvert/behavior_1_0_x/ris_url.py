from cffconvert.behavior_shared.ris_url_shared import RisUrlShared as Shared


class RisUrl(Shared):

    def __init__(self, cffobj):
        super().__init__(cffobj)

    def as_string(self):
        state = [
            ('I', False),
            ('R', self._has_repository()),
            ('A', self._has_repository_artifact()),
            ('C', self._has_repository_code()),
            ('U', self._has_url())
        ]
        key = ''.join([item[0] if item[1] is True else '_' for item in state])
        return self._behaviors[key]()
