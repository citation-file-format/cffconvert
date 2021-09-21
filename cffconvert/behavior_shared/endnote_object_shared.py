from abc import abstractmethod


class EndnoteObjectShared:

    supported_endnote_props = [
        'author',
        'year',
        'keyword',
        'doi',
        'name',
        'url'
    ]
    supported_cff_versions = None

    def __init__(self, cffobj, initialize_empty=False):
        self.cffobj = cffobj
        self.author = None
        self.doi = None
        self.keyword = None
        self.name = None
        self.url = None
        self.year = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def __str__(self):
        items = [item for item in [self.author,
                                   self.year,
                                   self.keyword,
                                   self.doi,
                                   self.name,
                                   self.url] if item is not None]
        return '%0 Generic\n' + ''.join(items)

    def add_all(self):
        self.add_author() \
            .add_doi() \
            .add_keyword() \
            .add_name() \
            .add_url() \
            .add_year()
        return self

    @abstractmethod
    def add_author(self):
        pass

    @abstractmethod
    def add_doi(self):
        pass

    def add_keyword(self):
        if 'keywords' in self.cffobj.keys():
            keywords = [f"%K {keyword}\n" for keyword in self.cffobj['keywords']]
            self.keyword = ''.join(keywords)
        return self

    def add_name(self):
        if 'title' in self.cffobj.keys():
            self.name = f"%T {self.cffobj['title']}\n"
        return self

    @abstractmethod
    def add_url(self):
        pass

    @abstractmethod
    def add_year(self):
        pass

    def as_string(self):
        return self.__str__()

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError("Expected cffobj to be of type 'dict'.")
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError("Missing key 'cff-version' in CITATION.cff file.")
        if self.cffobj['cff-version'] not in self.supported_cff_versions:
            raise ValueError(f"'cff-version': '{self.cffobj['cff-version']}' isn't a supported version.")
