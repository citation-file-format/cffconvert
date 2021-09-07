from cffconvert.behavior_shared.bibtex import BibtexAuthorShared
from cffconvert.behavior_shared.bibtex import BibtexObjectShared


class BibtexAuthor(BibtexAuthorShared):

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
            'FFF': BibtexAuthorShared._from_thin_air
        }

    def as_string(self):
        state = [
            self._exists_nonempty('given-names'),
            self._exists_nonempty('family-names'),
            self._exists_nonempty('name')
        ]
        key = ''.join(['T' if item is True else 'F' for item in state])
        return self._behaviors[key]()


class BibtexObject(BibtexObjectShared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj, initialize_empty)

    def add_author(self):
        authors_cff = self.cffobj.get('authors', list())
        authors_bibtex = [BibtexAuthor(a).as_string() for a in authors_cff]
        authors_bibtex_filtered = [a for a in authors_bibtex if a is not None]
        self.author = 'author = {' + ' and '.join(authors_bibtex_filtered) + '}'
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = 'doi = {' + self.cffobj['doi'] + '}'
        return self

    def add_month(self):
        if 'date-released' in self.cffobj.keys():
            self.month = 'month = {' + str(self.cffobj['date-released'].month) + '}'
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = 'year = {' + str(self.cffobj['date-released'].year) + '}'
        return self

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError("Expected cffobj to be of type 'dict'.")
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError("Missing key 'cff-version' in CITATION.cff file.")
        if self.cffobj['cff-version'] not in BibtexObject.supported_cff_versions:
            raise ValueError("cff-version: {} isn't a supported version."
                             .format(self.cffobj['cff-version']))
