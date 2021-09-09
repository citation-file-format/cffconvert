from cffconvert.behavior_shared.ris.author import RisAuthorShared as Shared


class RisAuthor(Shared):

    def __init__(self, author_cff):
        super().__init__(author_cff)

    def as_string(self):
        state = [
            ('G', self._exists_nonempty('given-names')),
            ('F', self._exists_nonempty('family-names')),
            ('A', False),
            ('N', self._exists_nonempty('name'))
        ]
        key = ''.join([item[0] if item[1] is True else '_' for item in state])
        return self._behaviors[key]()
