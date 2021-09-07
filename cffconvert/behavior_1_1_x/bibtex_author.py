from cffconvert.behavior_shared.bibtex_author import BibtexAuthorShared as Shared


class BibtexAuthor(Shared):

    def __init__(self, author_cff):
        super().__init__(author_cff)
        self._behaviors = {
            'TTTT': self._from_given_and_last,
            'TTTF': self._from_given_and_last,
            'TTFT': self._from_given_and_last,
            'TTFF': self._from_given_and_last,
            'TFTT': self._from_name,
            'TFTF': self._from_alias,
            'TFFT': self._from_name,
            'TFFF': self._from_given_only,
            'FTTT': self._from_last_only,
            'FTTF': self._from_last_only,
            'FTFT': self._from_last_only,
            'FTFF': self._from_last_only,
            'FFTT': self._from_name,
            'FFTF': self._from_alias,
            'FFFT': self._from_name,
            'FFFF': Shared._from_thin_air
        }

    def as_string(self):
        state = [
            self._exists_nonempty('given-names'),
            self._exists_nonempty('family-names'),
            self._exists_nonempty('alias'),
            self._exists_nonempty('name')
        ]
        key = ''.join(['T' if item is True else 'F' for item in state])
        return self._behaviors[key]()
