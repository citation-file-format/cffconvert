from abc import abstractmethod


# pylint: disable=too-many-instance-attributes
class SchemaorgObjectShared:

    supported_schemaorg_props = [
        "author",
        "codeRepository",
        "datePublished",
        "description",
        "identifier",
        "keywords",
        "license",
        "name",
        "url",
        "version"
    ]
    supported_cff_versions = None

    def __init__(self, cffobj):
        self.cffobj = cffobj
        self.author = None
        self.code_repository = None
        self.date_published = None
        self.description = None
        self.identifier = None
        self.keywords = None
        self.license = None
        self.name = None
        self.url = None
        self.version = None

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def add_all(self):
        pass

    @abstractmethod
    def add_author(self):
        pass

    @abstractmethod
    def add_date_published(self):
        pass

    def add_description(self):
        if "abstract" in self.cffobj.keys():
            self.description = self.cffobj["abstract"]
        return self

    @abstractmethod
    def add_identifier(self):
        pass

    def add_keywords(self):
        if "keywords" in self.cffobj.keys():
            self.keywords = self.cffobj["keywords"]
        return self

    def add_license(self):
        if "license" in self.cffobj.keys():
            self.license = f"https://spdx.org/licenses/{self.cffobj['license']}"
        return self

    def add_name(self):
        if "title" in self.cffobj.keys():
            self.name = self.cffobj["title"]
        return self

    @abstractmethod
    def add_urls(self):
        pass

    def add_version(self):
        if "version" in self.cffobj.keys():
            self.version = self.cffobj['version']
        return self

    def as_string(self):
        return self.__str__()

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError("Expected cffobj to be of type 'dict'.")
        if "cff-version" not in self.cffobj.keys():
            raise ValueError("Missing key 'cff-version' in CITATION.cff file.")
        if self.cffobj["cff-version"] not in self.supported_cff_versions:
            raise ValueError(f"'cff-version': '{self.cffobj['cff-version']}' isn't a supported version.")
