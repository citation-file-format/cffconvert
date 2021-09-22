from cffconvert.behavior_1_2_x.schemaorg_author import SchemaorgAuthor
from cffconvert.behavior_1_2_x.schemaorg_urls import SchemaorgUrls
from cffconvert.behavior_shared.schemaorg_object_shared import SchemaorgObjectShared as Shared


class SchemaorgObject(Shared):

    supported_cff_versions = [
        '1.2.0'
    ]

    def add_author(self):
        authors_cff = self.cffobj.get('authors', [])
        authors_schemaorg = [SchemaorgAuthor(a).as_dict() for a in authors_cff]
        self.author = [a for a in authors_schemaorg if a is not None]
        return self

    def add_date_published(self):
        if 'date-released' in self.cffobj.keys():
            self.date_published = self.cffobj['date-released']
        return self

    def add_identifier(self):
        if 'doi' in self.cffobj.keys():
            self.identifier = f"https://doi.org/{self.cffobj['doi']}"
        if 'identifiers' in self.cffobj.keys():
            identifiers = self.cffobj['identifiers']
            for identifier in identifiers:
                if identifier['type'] == 'doi':
                    self.identifier = f"https://doi.org/{identifier['value']}"
                    break
        return self

    def add_urls(self):
        self.code_repository, self.url = SchemaorgUrls(self.cffobj).as_tuple()
        return self
