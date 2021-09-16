from cffconvert.behavior_1_2_x.ris.author import RisAuthor
from cffconvert.behavior_1_2_x.ris.url import RisUrl
from cffconvert.behavior_shared.ris.ris import RisObjectShared as Shared


class RisObject(Shared):

    supported_cff_versions = [
        '1.2.0'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj, initialize_empty)

    def add_author(self):
        authors_cff = self.cffobj.get('authors', list())
        authors_bibtex = [RisAuthor(a).as_string() for a in authors_cff]
        authors_bibtex_filtered = [a for a in authors_bibtex if a is not None]
        self.author = ''.join(authors_bibtex_filtered)
        return self

    def add_date(self):
        if 'date-released' in self.cffobj.keys():
            self.date = 'DA  - {}\n'.format(self.cffobj['date-released'])
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = 'DO  - {}\n'.format(self.cffobj['doi'])
        if 'identifiers' in self.cffobj.keys():
            identifiers = self.cffobj['identifiers']
            for identifier in identifiers:
                if identifier['type'] == 'doi':
                    self.doi = 'DO  - {}\n'.format(identifier['value'])
                    break
        return self

    def add_url(self):
        self.url = RisUrl(self.cffobj).as_string()
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = 'PY  - {}\n'.format(self.cffobj['date-released'][:4])
        return self
