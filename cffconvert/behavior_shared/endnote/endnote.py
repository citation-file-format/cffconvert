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
            keywords = ['%K {}\n'.format(keyword) for keyword in self.cffobj['keywords']]
            self.keyword = ''.join(keywords)
        return self

    def add_name(self):
        if 'title' in self.cffobj.keys():
            self.name = '%T {}\n'.format(self.cffobj['title'])
        return self

    def add_url(self):
        if 'repository-code' in self.cffobj.keys():
            self.url = '%U {}\n'.format(self.cffobj['repository-code'])
        return self

    @abstractmethod
    def add_year(self):
        pass

    @abstractmethod
    def check_cffobj(self):
        pass

    def print(self):
        return self.__str__()
