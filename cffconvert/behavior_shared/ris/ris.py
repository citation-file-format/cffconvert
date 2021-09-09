from abc import abstractmethod


class RisObjectShared:

    supported_ris_props = [
        'abstract',
        'author',
        'date',
        'doi',
        'keywords',
        'title',
        'url',
        'year'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        self.cffobj = cffobj
        self.abstract = None
        self.author = None
        self.date = None
        self.doi = None
        self.keywords = None
        self.title = None
        self.url = None
        self.year = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def __str__(self):
        items = [item for item in [self.abstract,
                                   self.author,
                                   self.date,
                                   self.doi,
                                   self.keywords,
                                   self.year,
                                   self.title,
                                   self.url] if item is not None]
        return 'TY  - GEN\n' + ''.join(items) + 'ER\n'

    def add_all(self):
        self.add_abstract() \
            .add_author()   \
            .add_date()     \
            .add_doi()      \
            .add_keywords()  \
            .add_title()    \
            .add_url()      \
            .add_year()
        return self

    def add_abstract(self):
        if 'abstract' in self.cffobj.keys():
            self.abstract = 'AB  - {}\n'.format(self.cffobj['abstract'])
        return self

    @abstractmethod
    def add_author(self):
        pass

    @abstractmethod
    def add_date(self):
        pass

    @abstractmethod
    def add_doi(self):
        pass

    def add_keywords(self):
        if 'keywords' in self.cffobj.keys():
            keywords = ['KW  - {}\n'.format(keyword) for keyword in self.cffobj['keywords']]
            self.keywords = ''.join(keywords)
        return self

    def add_title(self):
        if 'title' in self.cffobj.keys():
            self.title = 'TI  - {}\n'.format(self.cffobj['title'])
        return self

    def add_url(self):
        if 'repository-code' in self.cffobj.keys():
            self.url = 'UR  - {}\n'.format(self.cffobj['repository-code'])
        return self

    @abstractmethod
    def add_year(self):
        pass

    @abstractmethod
    def check_cffobj(self):
        pass

    def print(self):
        return self.__str__()
