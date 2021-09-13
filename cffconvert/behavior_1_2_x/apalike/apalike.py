from cffconvert.behavior_1_2_x.apalike.author import ApalikeAuthor
from cffconvert.behavior_shared.apalike.apalike import ApalikeObjectShared as Shared


class ApalikeObject(Shared):

    supported_cff_versions = [
        '1.2.0'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj, initialize_empty)

    def add_author(self):
        authors_cff = self.cffobj.get('authors', list())
        authors_apalike = [ApalikeAuthor(a).as_string() for a in authors_cff]
        authors_apalike_filtered = [a for a in authors_apalike if a is not None]
        if len(authors_apalike_filtered) > 0:
            self.author = ', '.join(authors_apalike_filtered)
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = '(' + self.cffobj['date-released'].split('-')[0] + ').'
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = 'DOI: ' + self.cffobj['doi']
        if 'identifiers' in self.cffobj.keys():
            identifiers = self.cffobj['identifiers']
            for identifier in identifiers:
                if identifier['type'] == 'doi':
                    self.doi = 'DOI: ' + identifier['value']
                    break
        return self
