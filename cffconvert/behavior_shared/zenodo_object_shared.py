import json
from abc import abstractmethod


# pylint: disable=too-many-instance-attributes
class ZenodoObjectShared:

    supported_zenodo_props = [
        'creators',
        'description',
        'keywords',
        'license',
        'publication_date',
        'title',
        'version'
    ]
    supported_cff_versions = None

    def __init__(self, cffobj, initialize_empty=False):
        self.cffobj = cffobj
        self.creators = None
        self.description = None
        self.keywords = None
        self.license = None
        self.publication_date = None
        self.title = None
        self.version = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def __str__(self, sort_keys=True, indent=2):
        data = {
            "creators": self.creators,
            "description": self.description,
            "keywords": self.keywords,
            "license": self.license,
            "publication_date": self.publication_date,
            "title": self.title,
            "version": self.version
        }
        filtered = [item for item in data.items() if item[1] is not None]
        return json.dumps(dict(filtered), sort_keys=sort_keys, indent=indent, ensure_ascii=False) + '\n'

    def add_all(self):
        self.add_creators()          \
            .add_description()       \
            .add_keywords()          \
            .add_license()           \
            .add_publication_date()  \
            .add_title()             \
            .add_version()
        return self

    @abstractmethod
    def add_creators(self):
        pass

    def add_description(self):
        if 'abstract' in self.cffobj.keys():
            self.description = self.cffobj['abstract']
        return self

    def add_keywords(self):
        if 'keywords' in self.cffobj.keys():
            self.keywords = self.cffobj['keywords']
        return self

    def add_license(self):
        if 'license' in self.cffobj.keys():
            self.license = dict(id=self.cffobj['license'])
        return self

    @abstractmethod
    def add_publication_date(self):
        pass

    def add_title(self):
        if 'title' in self.cffobj.keys():
            self.title = self.cffobj['title']
        return self

    def add_version(self):
        if 'version' in self.cffobj.keys():
            self.version = self.cffobj['version']
        return self

    def as_string(self):
        return self.__str__()

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError("Expected cffobj to be of type 'dict'.")
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError("Missing key 'cff-version' in CITATION.cff file.")
        if self.cffobj['cff-version'] not in self.supported_cff_versions:
            raise ValueError(f"'cff-version': '{self.cffobj['cff-version']}' isn't a supported version.")
