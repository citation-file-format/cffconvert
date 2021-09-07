from cffconvert.behavior_shared.bibtex_author import BibtexAuthorShared as Shared


class BibtexAuthor(Shared):

    def __init__(self, author_cff):
        super().__init__(author_cff)
        self._behaviors = {
            'TTT': self._from_given_and_last,
            'TTF': self._from_given_and_last,
            'TFT': self._from_name,
            'TFF': self._from_given_only,
            'FTT': self._from_last_only,
            'FTF': self._from_last_only,
            'FFT': self._from_name,
            'FFF': Shared._from_thin_air
        }

    def as_string(self):
        state = [
            self._exists_nonempty('given-names'),
            self._exists_nonempty('family-names'),
            self._exists_nonempty('name')
        ]
        key = ''.join(['T' if item is True else 'F' for item in state])
        return self._behaviors[key]()
