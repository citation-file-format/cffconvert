from cffconvert.behavior_shared.schemaorg.author import SchemaorgAuthorShared as Shared


class SchemaorgAuthor(Shared):

    def __init__(self, author):
        super().__init__(author)

    def as_dict(self):
        state = [
            ('G', self._exists_nonempty('given-names')),
            ('F', self._exists_nonempty('family-names')),
            ('A', self._exists_nonempty('alias')),
            ('N', self._exists_nonempty('name')),
            ('A', self._exists_nonempty('affiliation')),
            ('O', self._exists_nonempty('orcid'))
        ]
        key = ''.join([item[0] if item[1] is True else '_' for item in state])
        return self._behaviors[key]()
