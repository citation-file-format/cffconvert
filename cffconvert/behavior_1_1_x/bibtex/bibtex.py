from cffconvert.behavior_1_1_x.bibtex.author import BibtexAuthor
from cffconvert.behavior_1_1_x.bibtex.url import BibtexUrl
from cffconvert.behavior_shared.bibtex.bibtex import BibtexObjectShared as Shared


class BibtexObject(Shared):

    supported_cff_versions = [
        '1.1.0'
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
        if 'identifiers' in self.cffobj.keys():
            identifiers = self.cffobj['identifiers']
            for identifier in identifiers:
                if identifier['type'] == 'doi':
                    self.doi = 'doi = {' + identifier['value'] + '}'
                    break
        return self

    def add_month(self):
        if 'date-released' in self.cffobj.keys():
            self.month = 'month = {' + str(self.cffobj['date-released'].month) + '}'
        return self

    def add_url(self):
        self.url = BibtexUrl(self.cffobj).as_string()
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = 'year = {' + str(self.cffobj['date-released'].year) + '}'
        return self
