from cffconvert.behavior_shared.zenodo_creator_shared import ZenodoCreatorShared as Shared


class ZenodoCreator(Shared):

    def __init__(self, author):
        super().__init__(author)

    def as_dict(self):
        key = ''.join([
            self._has_given_name(),
            self._has_family_name(),
            self._has_alias(),
            self._has_name(),
            self._has_affiliation(),
            self._has_orcid()
        ])
        return self._behaviors[key]()
