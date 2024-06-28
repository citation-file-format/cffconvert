from cffconvert.lib.cff_1_x_x.authors.biblatex import BiblatexAuthor
from cffconvert.lib.cff_1_x_x.biblatex import BiblatexObjectShared as Shared
from cffconvert.lib.cff_1_x_x.urls.biblatex import BiblatexUrl


class BiblatexObject(Shared):

    supported_cff_versions = [
        "1.0.1",
        "1.0.2",
        "1.0.3"
    ]

    def add_author(self):
        authors_cff = self.cffobj.get("authors", [])
        authors_biblatex = [BiblatexAuthor(a).as_string() for a in authors_cff]
        authors_biblatex_filtered = [a for a in authors_biblatex if a is not None]
        self.author = "author = {" + " and ".join(authors_biblatex_filtered) + "}"
        return self

    def add_doi(self):
        if "doi" in self.cffobj.keys():
            self.doi = "doi = {" + self.cffobj["doi"] + "}"
        return self

    def add_month(self):
        if "date-released" in self.cffobj.keys():
            self.month = "month = {" + str(self.cffobj["date-released"].month) + "}"
        return self

    def add_url(self):
        self.url = BiblatexUrl(self.cffobj).as_string()
        return self

    def add_year(self):
        if "date-released" in self.cffobj.keys():
            self.year = "year = {" + str(self.cffobj["date-released"].year) + "}"
        return self
