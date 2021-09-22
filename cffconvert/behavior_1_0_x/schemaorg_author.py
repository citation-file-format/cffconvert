from cffconvert.behavior_shared.schemaorg_author_shared import SchemaorgAuthorShared as Shared


# pylint: disable=too-few-public-methods
class SchemaorgAuthor(Shared):

    def as_dict(self):
        key = ''.join([
            self._has_given_name(),
            self._has_family_name(),
            '_',
            self._has_name(),
            self._has_affiliation(),
            self._has_orcid()
        ])
        return self._behaviors[key]()
