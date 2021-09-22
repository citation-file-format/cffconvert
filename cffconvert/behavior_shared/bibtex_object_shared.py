from abc import abstractmethod


class BibtexObjectShared:

    supported_bibtex_props = [
        'author',
        'doi',
        'month',
        'title',
        'url',
        'year'
    ]
    supported_cff_versions = None

    def __init__(self, cffobj, initialize_empty=False):
        self.cffobj = cffobj
        self.author = None
        self.doi = None
        self.month = None
        self.title = None
        self.url = None
        self.year = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def __str__(self, reference='YourReferenceHere'):
        items = [item for item in [self.author,
                                   self.doi,
                                   self.month,
                                   self.title,
                                   self.url,
                                   self.year] if item is not None]
        joined = ',\n'.join(items)
        return '@misc{' + reference + ',\n' + joined + '\n}\n'

    def add_all(self):
        self.add_author()   \
            .add_doi()      \
            .add_month()    \
            .add_title()    \
            .add_url()      \
            .add_year()
        return self

    @abstractmethod
    def add_author(self):
        pass

    @abstractmethod
    def add_doi(self):
        pass

    @abstractmethod
    def add_month(self):
        pass

    def add_title(self):
        if 'title' in self.cffobj.keys():
            self.title = 'title = {' + self.cffobj['title'] + '}'
        return self

    @abstractmethod
    def add_url(self):
        pass

    @abstractmethod
    def add_year(self):
        pass

    def as_string(self, reference='YourReferenceHere'):
        return self.__str__(reference)

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError("Expected cffobj to be of type 'dict'.")
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError("Missing key 'cff-version' in CITATION.cff file.")
        if self.cffobj['cff-version'] not in self.supported_cff_versions:
            raise ValueError(f"cff-version: {self.cffobj['cff-version']} isn't a supported version.")
