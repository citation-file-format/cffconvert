import json
from cffconvert.behavior_1_2_x.zenodo_creator import ZenodoCreator
from cffconvert.behavior_shared.zenodo_object_shared import ZenodoObjectShared as Shared


class ZenodoObject(Shared):

    supported_cff_versions = [
        "1.2.0"
    ]
    supported_zenodo_props = Shared.supported_zenodo_props + [
        "upload_type"
    ]

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj)
        self.upload_type = None
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
            "upload_type": self.upload_type,
            "version": self.version
        }
        filtered = [item for item in data.items() if item[1] is not None]
        return json.dumps(dict(filtered), sort_keys=sort_keys, indent=indent, ensure_ascii=False) + "\n"

    def add_all(self):
        self.add_creators()          \
            .add_description()       \
            .add_keywords()          \
            .add_license()           \
            .add_publication_date()  \
            .add_title()             \
            .add_upload_type()       \
            .add_version()
        return self

    def add_creators(self):
        authors_cff = self.cffobj.get("authors", [])
        creators_zenodo = [ZenodoCreator(a).as_dict() for a in authors_cff]
        self.creators = [c for c in creators_zenodo if c is not None]
        return self

    def add_publication_date(self):
        if "date-released" in self.cffobj.keys():
            self.publication_date = self.cffobj["date-released"]
        return self

    def add_upload_type(self):
        if "type" in self.cffobj.keys():
            if self.cffobj["type"] == "software":
                self.upload_type = "software"
            if self.cffobj["type"] == "dataset":
                self.upload_type = "dataset"
        return self
