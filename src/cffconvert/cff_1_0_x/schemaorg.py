import json
from cffconvert.cff_1_x_x.authors.schemaorg import SchemaorgAuthor
from cffconvert.cff_1_x_x.schemaorg import SchemaorgObjectShared as Shared
from cffconvert.cff_1_x_x.urls.schemaorg import SchemaorgUrls


class SchemaorgObject(Shared):

    supported_cff_versions = [
        "1.0.1",
        "1.0.2",
        "1.0.3"
    ]
    supported_schemaorg_props = Shared.supported_schemaorg_props + [
        "@context"
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

    def __str__(self, sort_keys=True, indent=2):
        data = {
            "@context": self.context,
            "@type": "SoftwareSourceCode",
            "author": self.author,
            "codeRepository": self.code_repository,
            "datePublished": self.date_published,
            "description": self.description,
            "identifier": self.identifier,
            "keywords": self.keywords,
            "license": self.license,
            "name": self.name,
            "url": self.url,
            "version": self.version
        }
        filtered = [item for item in data.items() if item[1] is not None]
        return json.dumps(dict(filtered), sort_keys=sort_keys, indent=indent, ensure_ascii=False) + "\n"

    def add_all(self):
        self.add_author()           \
            .add_date_published()   \
            .add_description()      \
            .add_identifier()       \
            .add_keywords()         \
            .add_license()          \
            .add_name()             \
            .add_urls()             \
            .add_version()
        return self

    def add_author(self):
        authors_cff = self.cffobj.get("authors", [])
        authors_schemaorg = [SchemaorgAuthor(a).as_dict() for a in authors_cff]
        self.author = [a for a in authors_schemaorg if a is not None]
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

    def add_urls(self):
        self.code_repository, self.url = SchemaorgUrls(self.cffobj).as_tuple()
        return self
