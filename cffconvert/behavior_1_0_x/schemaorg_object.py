from cffconvert.behavior_1_0_x.schemaorg_author import SchemaorgAuthor
from cffconvert.behavior_1_0_x.schemaorg_urls import SchemaorgUrls
from cffconvert.behavior_shared.schemaorg_object_shared import SchemaorgObjectShared as Shared


class SchemaorgObject(Shared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def add_author(self):
        authors_cff = self.cffobj.get('authors', [])
        authors_schemaorg = [SchemaorgAuthor(a).as_dict() for a in authors_cff]
        self.author = [a for a in authors_schemaorg if a is not None]
        return self

    def add_date_published(self):
        if 'date-released' in self.cffobj.keys():
            year = self.cffobj['date-released'].year
            month = self.cffobj['date-released'].month
            day = self.cffobj['date-released'].day
            self.date_published = f"{year:d}-{month:02d}-{day:02d}"
        return self

    def add_identifier(self):
        if 'doi' in self.cffobj.keys():
            self.identifier = f"https://doi.org/{self.cffobj['doi']}"
        return self

    def add_urls(self):
        self.code_repository, self.url = SchemaorgUrls(self.cffobj).as_tuple()
        return self
