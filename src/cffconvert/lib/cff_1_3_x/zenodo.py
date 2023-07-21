from cffconvert.lib.cff_1_x_x.authors.zenodo import ZenodoAuthor
from cffconvert.lib.cff_1_x_x.zenodo import ZenodoObjectShared as Shared


class ZenodoObject(Shared):

    supported_cff_versions = [
        "1.3.0"
    ]

    def add_contributors(self):
        contributors = []
        for c in self.cffobj.get("contributors", []):
            # contributors are generated in the same way as authors, hence just
            # call ZenodoAuthor's contructor with the cff contributor object
            contributor = ZenodoAuthor(c).as_dict()
            contributor.update({"type": "Other"})
            contributors.append(contributor)
        # filter out contributors that had no data associated with them
        contributors = [c for c in contributors if c is not None]
        if len(contributors) > 0:
            self.contributors = contributors
        return self

    def add_creators(self):
        authors_cff = self.cffobj.get("authors", [])
        creators_zenodo = [ZenodoAuthor(a).as_dict() for a in authors_cff]
        self.creators = [c for c in creators_zenodo if c is not None]
        return self

    def add_publication_date(self):
        if "date-released" in self.cffobj.keys():
            self.publication_date = self.cffobj["date-released"]
        return self

    def add_upload_type(self):
        typ = self.cffobj.get("type", "")
        if typ == "dataset":
            self.upload_type = "dataset"
        elif typ == "software":
            self.upload_type = "software"
        else:
            # default value for type is 'software'
            self.upload_type = "software"
        return self
