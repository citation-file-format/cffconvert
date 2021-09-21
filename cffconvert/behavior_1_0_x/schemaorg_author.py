from cffconvert.behavior_shared.schemaorg_author_shared import SchemaorgAuthorShared as Shared


class SchemaorgAuthor(Shared):

    def __init__(self, author):
        super().__init__(author)

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
