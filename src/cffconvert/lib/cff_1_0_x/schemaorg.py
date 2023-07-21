from cffconvert.lib.cff_1_x_x.authors.schemaorg import SchemaorgAuthor
from cffconvert.lib.cff_1_x_x.schemaorg import SchemaorgObjectShared as Shared
from cffconvert.lib.cff_1_x_x.urls.schemaorg import SchemaorgUrls


class SchemaorgObject(Shared):

    supported_cff_versions = [
        "1.0.1",
        "1.0.2",
        "1.0.3"
    ]

    def __init__(self, cffobj, context="https://schema.org", initialize_empty=False):
        super().__init__(cffobj)
        self.context = context
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def add_author(self):
        authors_cff = self.cffobj.get("authors", [])
        authors_schemaorg = [SchemaorgAuthor(a).as_dict() for a in authors_cff]
        self.author = [a for a in authors_schemaorg if a is not None]
        return self

    def add_contributor(self):
        # CFF v1.0.x doesn't have contributors
        return self

    def add_date_published(self):
        if "date-released" in self.cffobj.keys():
            year = self.cffobj["date-released"].year
            month = self.cffobj["date-released"].month
            day = self.cffobj["date-released"].day
            self.date_published = f"{year:d}-{month:02d}-{day:02d}"
        return self

    def add_identifier(self):
        if "doi" in self.cffobj.keys():
            self.identifier = f"https://doi.org/{self.cffobj['doi']}"
        return self

    def add_type(self):
        # CFF v1.0.x assumes the metadata describes software
        self.type = "SoftwareSourceCode"
        return self

    def add_urls(self):
        self.code_repository, self.url = SchemaorgUrls(self.cffobj).as_tuple()
        return self
