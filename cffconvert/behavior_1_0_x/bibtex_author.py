from cffconvert.behavior_shared.bibtex_author import BibtexAuthorShared as Shared


class BibtexAuthor(Shared):

    def __init__(self, author_cff):
        super().__init__(author_cff)
        self._behaviors = {
            'GFN': self._from_given_and_last,
            'GF.': self._from_given_and_last,
            'G.N': self._from_name,
            'G..': self._from_given,
            '.FN': self._from_last,
            '.F.': self._from_last,
            '..N': self._from_name,
            '...': Shared._from_thin_air
        }

    def as_string(self):
        state = [
            ('G', self._exists_nonempty('given-names')),
            ('F', self._exists_nonempty('family-names')),
            ('N', self._exists_nonempty('name'))
        ]
        key = ''.join([item[0] if item[1] is True else '.' for item in state])
        return self._behaviors[key]()
