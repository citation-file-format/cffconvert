from cffconvert.behavior_1_2_x.zenodo_creator import ZenodoCreator
from cffconvert.behavior_shared.zenodo_object_shared import ZenodoObjectShared as Shared


class ZenodoObject(Shared):

    supported_cff_versions = [
        '1.2.0'
    ]

    def add_creators(self):
        authors_cff = self.cffobj.get('authors', [])
        creators_zenodo = [ZenodoCreator(a).as_dict() for a in authors_cff]
        self.creators = [c for c in creators_zenodo if c is not None]
        return self

    def add_publication_date(self):
        if 'date-released' in self.cffobj.keys():
            self.publication_date = self.cffobj['date-released']
        return self
