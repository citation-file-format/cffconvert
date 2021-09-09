from cffconvert.behavior_1_0_x.schemaorg.author import SchemaorgAuthor
from cffconvert.behavior_shared.schemaorg.schemaorg import SchemaorgObjectShared as Shared


class SchemaorgObject(Shared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def __init__(self, cffobj, initialize_empty=False, context="https://schema.org"):
        super().__init__(cffobj, initialize_empty, context)

    def add_author(self):
        authors_cff = self.cffobj.get('authors', list())
        authors_schemaorg = [SchemaorgAuthor(a).as_dict() for a in authors_cff]
        self.author = [a for a in authors_schemaorg if a is not None]
        return self

    def add_date_published(self):
        if 'date-released' in self.cffobj.keys():
            self.date_published = "{:d}-{:02d}-{:02d}".format(self.cffobj['date-released'].year,
                                                              self.cffobj['date-released'].month,
                                                              self.cffobj['date-released'].day)
        return self

    def add_identifier(self):
        if 'doi' in self.cffobj.keys():
            self.identifier = 'https://doi.org/{}'.format(self.cffobj['doi'])
        return self

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError('Expected cffobj to be of type \'dict\'.')
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        if self.cffobj['cff-version'] not in SchemaorgObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cffobj['cff-version']))
