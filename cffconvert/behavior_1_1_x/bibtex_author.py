from cffconvert.behavior_shared.bibtex_author_shared import BibtexAuthorShared as Shared


class BibtexAuthor(Shared):

    def __init__(self, author):
        super().__init__(author)

    def as_string(self):
        state = [
            ('G', self._exists_nonempty('given-names')),
            ('F', self._exists_nonempty('family-names')),
            ('A', self._exists_nonempty('alias')),
            ('N', self._exists_nonempty('name'))
        ]
        key = ''.join([item[0] if item[1] is True else '_' for item in state])
        return self._behaviors[key]()
