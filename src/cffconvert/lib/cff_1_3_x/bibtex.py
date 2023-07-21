from cffconvert.lib.cff_1_x_x.authors.bibtex import BibtexAuthor
from cffconvert.lib.cff_1_x_x.bibtex import BibtexObjectShared as Shared
from cffconvert.lib.cff_1_x_x.urls.bibtex import BibtexUrl


class BibtexObject(Shared):

    supported_cff_versions = [
        "1.3.0"
    ]

    def add_author(self):
        authors_cff = self.cffobj.get("authors", [])
        authors_bibtex = [BibtexAuthor(a).as_string() for a in authors_cff]
        authors_bibtex_filtered = [a for a in authors_bibtex if a is not None]
        self.author = "author = {" + " and ".join(authors_bibtex_filtered) + "}"
        return self

    def add_doi(self):
        if "doi" in self.cffobj.keys():
            self.doi = "doi = {" + self.cffobj["doi"] + "}"
        if "identifiers" in self.cffobj.keys():
            identifiers = self.cffobj["identifiers"]
            for identifier in identifiers:
                if identifier["type"] == "doi":
                    self.doi = "doi = {" + identifier["value"] + "}"
                    break
        return self

    def add_month(self):
        if "date-released" in self.cffobj.keys():
            month = self.cffobj["date-released"].split("-")[1].lstrip("0")
            self.month = "month = {" + month + "}"
        return self

    def add_url(self):
        self.url = BibtexUrl(self.cffobj).as_string()
        return self

    def add_year(self):
        if "date-released" in self.cffobj.keys():
            self.year = "year = {" + self.cffobj["date-released"][:4] + "}"
        return self
