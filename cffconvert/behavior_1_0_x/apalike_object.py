from cffconvert.behavior_1_0_x.apalike_author import ApalikeAuthor
from cffconvert.behavior_1_0_x.apalike_url import ApalikeUrl
from cffconvert.behavior_shared.apalike.apalike import ApalikeObjectShared as Shared


class ApalikeObject(Shared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
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
            self.year = '(' + str(self.cffobj['date-released'].year) + ').'
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = 'DOI: ' + self.cffobj['doi']
        return self

    def add_url(self):
        self.url = ApalikeUrl(self.cffobj).as_string()
        return self
