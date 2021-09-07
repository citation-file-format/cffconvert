from abc import abstractmethod


class BibtexAuthorShared:

    def __init__(self, author_cff):
        self._author_cff = author_cff
        self._behaviors = None

    def _exists_nonempty(self, key):
        value = self._author_cff.get(key, None)
        return value is not None and value != ''

    def _from_alias(self):
        return self._author_cff.get('alias')

    def _from_given_and_last(self):
        return self._from_last_only() + ", " + self._from_given_only()

    def _from_given_only(self):
        return self._author_cff.get('given-names')

    def _from_last_only(self):
        nameparts = [
            self._author_cff.get('name-particle'),
            self._author_cff.get('family-names'),
            self._author_cff.get('name-suffix')
        ]
        return ' '.join([n for n in nameparts if n is not None])

    def _from_name(self):
        return self._author_cff.get('name')

    @staticmethod
    def _from_thin_air():
        return None


class BibtexObjectShared:

    supported_bibtex_props = [
        'author',
        'doi',
        'month',
        'title',
        'url',
        'year'
    ]

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
        s = ',\n'.join(items)
        return '@misc{' + reference + ',\n' + s + '\n}\n'

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

    def add_url(self):
        if 'repository-code' in self.cffobj.keys():
            self.url = 'url = {' + self.cffobj['repository-code'] + '}'
        return self

    @abstractmethod
    def add_year(self):
        pass

    @abstractmethod
    def check_cffobj(self):
        pass

    def print(self, reference='YourReferenceHere'):
        return self.__str__(reference)
