from cffconvert.behavior_shared.apalike_author_shared import ApalikeAuthorShared as Shared


# pylint: disable=too-few-public-methods
class ApalikeAuthor(Shared):

    def as_string(self):
        key = ''.join([
            self._has_given_name(),
            self._has_family_name(),
            self._has_alias(),
            self._has_name()
        ])
        return self._behaviors[key]()
