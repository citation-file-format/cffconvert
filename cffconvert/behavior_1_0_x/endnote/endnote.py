from cffconvert.behavior_1_1_x.endnote.author import EndnoteAuthor
from cffconvert.behavior_shared.endnote.endnote import EndnoteObjectShared as Shared


class EndnoteObject(Shared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj, initialize_empty)

    def add_author(self):
        authors_cff = self.cffobj.get('authors', list())
        authors_endnote = [EndnoteAuthor(a).as_string() for a in authors_cff]
        authors_endnote_filtered = [a for a in authors_endnote if a is not None]
        self.author = ''.join(authors_endnote_filtered)
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = '%R {}\n'.format(self.cffobj['doi'])
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = '%D {}\n'.format(self.cffobj['date-released'].year)
        return self
