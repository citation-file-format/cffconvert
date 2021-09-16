from cffconvert.behavior_1_0_x.zenodo_creator import ZenodoCreator
from cffconvert.behavior_shared.zenodo.zenodo import ZenodoObjectShared as Shared


class ZenodoObject(Shared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj, initialize_empty)

    def add_creators(self):
        authors_cff = self.cffobj.get('authors', list())
        creators_zenodo = [ZenodoCreator(a).as_dict() for a in authors_cff]
        self.creators = [c for c in creators_zenodo if c is not None]
        return self

    def add_publication_date(self):
        if 'date-released' in self.cffobj.keys():
            self.publication_date = '{:d}-{:02d}-{:02d}'.format(self.cffobj['date-released'].year,
                                                                self.cffobj['date-released'].month,
                                                                self.cffobj['date-released'].day)
        return self
