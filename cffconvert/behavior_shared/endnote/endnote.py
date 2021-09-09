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
        return '%0 Generic\n' + ''.join(items) + '%9 source code\n'

    def add_all(self):
        self.add_author() \
            .add_doi() \
            .add_keyword() \
            .add_name() \
            .add_url() \
            .add_year()
        return self

    def add_author(self):
        if 'authors' in self.cffobj.keys():
            authors = list()
            for author in self.cffobj['authors']:
                keys = author.keys()
                nameparts = [
                    author['name-particle'] if 'name-particle' in keys else None,
                    author['family-names'] if 'family-names' in keys else None,
                    author['name-suffix'] if 'name-suffix' in keys else None
                ]
                tmp = ' '.join([namepart for namepart in nameparts if namepart is not None])
                fullname = tmp + ', ' + author['given-names'] if 'given-names' in keys else tmp
                alias = author['alias'] if 'alias' in keys and author['alias'] is not None and author['alias'] != '' else None
                if fullname:
                    authors.append('%A {}\n'.format(fullname))
                elif alias:
                    authors.append('%A {}\n'.format(alias))
                else:
                    continue
            self.author = ''.join(authors)
        return self

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
