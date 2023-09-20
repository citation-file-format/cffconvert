from cffconvert.lib.cff_1_x_x.apalike import ApalikeObjectShared as Shared
from cffconvert.lib.cff_1_x_x.authors.apalike import ApalikeAuthor
from cffconvert.lib.cff_1_x_x.urls.apalike import ApalikeUrl


class ApalikeObject(Shared):

    supported_cff_versions = [
        "1.2.0"
    ]

    def add_author(self):
        authors_cff = self.cffobj.get("authors", [])
        authors_apalike = [ApalikeAuthor(a).as_string() for a in authors_cff]
        authors_apalike_filtered = [a for a in authors_apalike if a is not None]
        n_authors = len(authors_apalike_filtered)
        if n_authors < 1:
            # no need for joining authors when n_authors == 1
            pass
        elif n_authors == 1:
            self.author = ", ".join(authors_apalike_filtered)
        elif n_authors == 2:
            self.author = ", ".join(authors_apalike_filtered[:-1]) + " and " + authors_apalike_filtered[-1]
        else:
            self.author = ", ".join(authors_apalike_filtered[:-1]) + ", and " + authors_apalike_filtered[-1]
        return self

    def add_year(self):
        if "date-released" in self.cffobj.keys():
            self.year = "(" + self.cffobj["date-released"].split("-")[0] + ")."
        return self

    def add_doi(self):
        if "doi" in self.cffobj.keys():
            self.doi = "DOI: " + self.cffobj["doi"]
        if "identifiers" in self.cffobj.keys():
            identifiers = self.cffobj["identifiers"]
            for identifier in identifiers:
                if identifier["type"] == "doi":
                    self.doi = "DOI: " + identifier["value"]
                    break
        return self

    def add_url(self):
        self.url = ApalikeUrl(self.cffobj).as_string()
        return self
