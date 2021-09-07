from cffconvert.behavior_shared.bibtex_author import BibtexAuthorShared as Shared


class BibtexAuthor(Shared):

    def __init__(self, author_cff):
        super().__init__(author_cff)
        self._behaviors = {
            'GFAN': self._from_given_and_last,
            'GFA.': self._from_given_and_last,
            'GF.N': self._from_given_and_last,
            'GF..': self._from_given_and_last,
            'G.AN': self._from_name,
            'G.A.': self._from_alias,
            'G..N': self._from_name,
            'G...': self._from_given_only,
            '.FAN': self._from_last_only,
            '.FA.': self._from_last_only,
            '.F.N': self._from_last_only,
            '.F..': self._from_last_only,
            '..AN': self._from_name,
            '..A.': self._from_alias,
            '...N': self._from_name,
            '....': Shared._from_thin_air
        }

    def as_string(self):
        state = [
            ('G', self._exists_nonempty('given-names')),
            ('F', self._exists_nonempty('family-names')),
            ('A', self._exists_nonempty('alias')),
            ('N', self._exists_nonempty('name'))
        ]
        key = ''.join([item[0] if item[1] is True else '.' for item in state])
        return self._behaviors[key]()
