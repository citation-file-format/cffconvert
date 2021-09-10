from cffconvert.behavior_1_2_x.endnote.author import EndnoteAuthor
from cffconvert.behavior_shared.endnote.endnote import EndnoteObjectShared as Shared


class EndnoteObject(Shared):

    supported_cff_versions = [
        '1.2.0'
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
        if 'identifiers' in self.cffobj.keys():
            identifiers = self.cffobj['identifiers']
            for identifier in identifiers:
                if identifier['type'] == 'doi':
                    self.doi = '%R {}\n'.format(identifier['value'])
                    break
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = '%D {}\n'.format(self.cffobj['date-released'][:4])
        return self

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError('Expected cffobj to be of type \'dict\'.')
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        if self.cffobj['cff-version'] not in EndnoteObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cffobj['cff-version']))
