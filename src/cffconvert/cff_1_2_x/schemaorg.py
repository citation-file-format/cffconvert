import json
from cffconvert.cff_1_x_x.authors.schemaorg import SchemaorgAuthor
from cffconvert.cff_1_x_x.schemaorg import SchemaorgObjectShared as Shared
from cffconvert.cff_1_x_x.urls.schemaorg import SchemaorgUrls


class SchemaorgObject(Shared):

    supported_cff_versions = [
        "1.2.0"
    ]
    supported_schemaorg_props = Shared.supported_schemaorg_props + [
        "@context",
        "@type"
    ]

    def __init__(self, cffobj, context="https://schema.org", initialize_empty=False):
        super().__init__(cffobj)
        self.context = context
        self.type = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def __str__(self, sort_keys=True, indent=2):
        data = {
            "@context": self.context,
            "@type": self.type,
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
            .add_type()             \
            .add_urls()             \
            .add_version()
        return self

    def add_author(self):
        authors_cff = self.cffobj.get("authors", [])
        authors_schemaorg = [SchemaorgAuthor(a).as_dict() for a in authors_cff]
        self.author = [a for a in authors_schemaorg if a is not None]
        return self

    def add_contributor(self):
        # CFF v1.2.x doesn't have contributors
        pass

    def add_date_published(self):
        if "date-released" in self.cffobj.keys():
            self.date_published = self.cffobj["date-released"]
        return self

    def add_identifier(self):
        if "doi" in self.cffobj.keys():
            self.identifier = f"https://doi.org/{self.cffobj['doi']}"
        if "identifiers" in self.cffobj.keys():
            identifiers = self.cffobj["identifiers"]
            for identifier in identifiers:
                if identifier["type"] == "doi":
                    self.identifier = f"https://doi.org/{identifier['value']}"
                    break
        return self

    def add_type(self):
        typ = self.cffobj.get("type", "")
        if typ == "dataset":
            self.type = "Dataset"
        elif typ == "software":
            self.type = "SoftwareSourceCode"
        else:
            # default value for 'type' is 'software'
            self.type = "SoftwareSourceCode"
        return self

    def add_urls(self):
        self.code_repository, self.url = SchemaorgUrls(self.cffobj).as_tuple()
        # schema.org does not specify a target conversion key for
        # repository-code when type == 'dataset', so remove it
        if self.cffobj.get("type", "") == "dataset":
            self.code_repository = None
        return self
