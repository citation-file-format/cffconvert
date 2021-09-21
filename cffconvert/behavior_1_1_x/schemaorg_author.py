from cffconvert.behavior_shared.schemaorg_author_shared import SchemaorgAuthorShared as Shared


class SchemaorgAuthor(Shared):

    def __init__(self, author):
        super().__init__(author)

    def as_dict(self):
        state = [
            ('G', self._has_given_name()),
            ('F', self._has_family_name()),
            ('A', self._has_alias()),
            ('N', self._has_name()),
            ('A', self._has_affiliation()),
            ('O', self._has_orcid())
        ]
        key = ''.join([item[0] if item[1] is True else '_' for item in state])
        return self._behaviors[key]()
