from cffconvert.behavior_shared.bibtex_author_shared import BibtexAuthorShared as Shared


class BibtexAuthor(Shared):

    def __init__(self, author):
        super().__init__(author)

    def as_string(self):
        state = [
            ('G', self._has_given_name()),
            ('F', self._has_family_name()),
            ('A', self._has_alias()),
            ('N', self._has_name())
        ]
        key = ''.join([item[0] if item[1] is True else '_' for item in state])
        return self._behaviors[key]()
