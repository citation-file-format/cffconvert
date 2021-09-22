from cffconvert.behavior_shared.ris_author_shared import RisAuthorShared as Shared


# pylint: disable=too-few-public-methods
class RisAuthor(Shared):

    def as_string(self):
        key = ''.join([
            self._has_given_name(),
            self._has_family_name(),
            self._has_alias(),
            self._has_name()
        ])
        return self._behaviors[key]()
