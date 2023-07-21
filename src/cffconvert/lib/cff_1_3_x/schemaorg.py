from cffconvert.lib.cff_1_x_x.authors.schemaorg import SchemaorgAuthor
from cffconvert.lib.cff_1_x_x.schemaorg import SchemaorgObjectShared as Shared
from cffconvert.lib.cff_1_x_x.urls.schemaorg import SchemaorgUrls


# pylint: disable=too-many-instance-attributes
class SchemaorgObject(Shared):

    supported_cff_versions = [
        "1.3.0"
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
        contributors = [SchemaorgAuthor(c).as_dict() for c in self.cffobj.get("contributors", [])]
        contributors = [c for c in contributors if c is not None]
        if len(contributors) > 0:
            self.contributor = contributors
        return self

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
