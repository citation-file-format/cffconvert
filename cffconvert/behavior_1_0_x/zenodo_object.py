import json
from cffconvert.behavior_1_0_x.zenodo_creator import ZenodoCreator
from cffconvert.behavior_shared.zenodo_object_shared import ZenodoObjectShared as Shared


class ZenodoObject(Shared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj)
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

    def add_creators(self):
        authors_cff = self.cffobj.get('authors', [])
        creators_zenodo = [ZenodoCreator(a).as_dict() for a in authors_cff]
        self.creators = [c for c in creators_zenodo if c is not None]
        return self

    def add_publication_date(self):
        if 'date-released' in self.cffobj.keys():
            year = self.cffobj['date-released'].year
            month = self.cffobj['date-released'].month
            day = self.cffobj['date-released'].day
            self.publication_date = f"{year:d}-{month:02d}-{day:02d}"
        return self
