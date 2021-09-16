from cffconvert.behavior_1_1_x.schemaorg_author import SchemaorgAuthor
from cffconvert.behavior_1_1_x.schemaorg_urls import SchemaorgUrls
from cffconvert.behavior_shared.schemaorg_object_shared import SchemaorgObjectShared as Shared


class SchemaorgObject(Shared):

    supported_cff_versions = [
        '1.1.0'
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
        if 'identifiers' in self.cffobj.keys():
            identifiers = self.cffobj['identifiers']
            for identifier in identifiers:
                if identifier['type'] == 'doi':
                    self.identifier = 'https://doi.org/{}'.format(identifier['value'])
                    break
        return self

    def add_urls(self):
        self.code_repository, self.url = SchemaorgUrls(self.cffobj).as_tuple()
        return self
