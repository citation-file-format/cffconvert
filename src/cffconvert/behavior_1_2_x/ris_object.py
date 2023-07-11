from cffconvert.behavior_1_2_x.ris_author import RisAuthor
from cffconvert.behavior_1_2_x.ris_url import RisUrl
from cffconvert.behavior_shared.ris_object_shared import RisObjectShared as Shared


class RisObject(Shared):

    supported_cff_versions = [
        '1.2.0'
    ]

    def add_author(self):
        authors_cff = self.cffobj.get('authors', [])
        authors_bibtex = [RisAuthor(a).as_string() for a in authors_cff]
        authors_bibtex_filtered = [a for a in authors_bibtex if a is not None]
        self.author = ''.join(authors_bibtex_filtered)
        return self

    def add_date(self):
        if 'date-released' in self.cffobj.keys():
            self.date = f"DA  - {self.cffobj['date-released']}\n"
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = f"DO  - {self.cffobj['doi']}\n"
        if 'identifiers' in self.cffobj.keys():
            identifiers = self.cffobj['identifiers']
            for identifier in identifiers:
                if identifier['type'] == 'doi':
                    self.doi = f"DO  - {identifier['value']}\n"
                    break
        return self

    def add_url(self):
        self.url = RisUrl(self.cffobj).as_string()
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = f"PY  - {self.cffobj['date-released'][:4]}\n"
        return self
