from abc import abstractmethod


class BiblatexObjectShared:

    supported_cff_versions = None

    def __init__(self, cffobj, initialize_empty=False):
        self.cffobj = cffobj
        self.author = None
        self.doi = None
        self.month = None
        self.title = None
        self.url = None
        self.year = None
        # below are new added fields not supported by bibtex
        self.abstract = None
        self.date = None
        self.repository = None
        self.license = None
        self.version = None
        self.institution = None
        self.editor = None
        self.swhid = None
        self.keywords = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def __str__(self):
        items = [item for item in [self.author,
                                   self.doi,
                                   self.month,
                                   self.title,
                                   self.url,
                                   self.year,
                                   self.abstract,
                                   self.date,
                                   self.repository,
                                   self.license,
                                   self.version,
                                   self.institution,
                                   self.editor,
                                   self.swhid,
                                   self.keywords] if item is not None]
        joined = ",\n".join(items)
        return "@software{YourReferenceHere,\n" + joined + "\n}\n"

    def add_all(self):
        self.add_author()     \
            .add_doi()        \
            .add_month()      \
            .add_title()      \
            .add_url()        \
            .add_year()       \
            .add_abstract()   \
            .add_date()       \
            .add_repository() \
            .add_license()    \
            .add_version()    \
            .add_institution()\
            .add_editor()     \
            .add_swhid()      \
            .add_keywords()

        return self

    @abstractmethod
    def add_author(self):
        pass

    @abstractmethod
    def add_doi(self):
        pass

    @abstractmethod
    def add_month(self):
        pass

    def add_title(self):
        if "title" in self.cffobj.keys():
            self.title = "title = {" + self.cffobj["title"] + "}"
        return self

    @abstractmethod
    def add_url(self):
        pass

    @abstractmethod
    def add_year(self):
        pass

    def add_abstract(self):
        if "abstract" in self.cffobj.keys():
            self.abstract = "abstract = {" + self.cffobj["abstract"] + "}"
        return self

    @abstractmethod
    def add_date(self):
        pass

    def add_repository(self):
        if "repository-code" in self.cffobj.keys():
            self.repository = "repository = {" + self.cffobj["repository-code"] + "}"
        if "repository" in self.cffobj.keys():
            self.repository = "repository = {" + self.cffobj["repository"] + "}"
        return self

    def add_license(self):
        if "license" in self.cffobj.keys():
            self.license = "license = {" + self.cffobj["license"] + "}"
        return self

    def add_version(self):
        if "version" in self.cffobj.keys():
            self.version = "version = {" + self.cffobj["version"] + "}"
        return self

    def add_institution(self):
        if "contact" in self.cffobj.keys():
            for contact in self.cffobj["contact"]:
                if "name" in contact:
                    self.institution = "institution = {" + contact["name"] + "}"
                    break
        return self

    def add_editor(self):
        if "contact" in self.cffobj.keys():
            editors = [i["family-names"] + ", " + i["given-names"]
                          for i in self.cffobj["contact"]
                              if "name" not in i and "given-names" in i and "family-names" in i]
            if editors:
                self.editor = "editor = {" + " and ".join(editors) + "}"
        return self

    def add_swhid(self):
        if "identifiers" in self.cffobj.keys():
            for identifier in self.cffobj["identifiers"]:
                if identifier["type"] == "swh":
                    self.swhid = "swhid = {" + identifier["value"] + "}"
                    break
        return self

    def add_keywords(self):
        if "keywords" in self.cffobj.keys():
            self.keywords = "keywords = {" + ", ".join(self.cffobj["keywords"]) + "}"
        return self

    def as_string(self):
        return str(self)

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError("Expected cffobj to be of type 'dict'.")
        if "cff-version" not in self.cffobj.keys():
            raise ValueError("Missing key 'cff-version' in CITATION.cff file.")
        if self.cffobj["cff-version"] not in self.supported_cff_versions:
            raise ValueError(f"cff-version: {self.cffobj['cff-version']} isn't a supported version.")
