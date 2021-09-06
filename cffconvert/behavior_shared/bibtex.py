from abc import abstractmethod


def _author_cff_to_author_bibtex(author_cff):
    has_given_names = _exists_nonempty(author_cff, 'given-names')
    has_family_names = _exists_nonempty(author_cff, 'family-names')
    has_alias = _exists_nonempty(author_cff, 'alias')
    has_name = _exists_nonempty(author_cff, 'name')

    return {
        (True, True, True, True): _from_given_and_last,
        (True, True, True, False): _from_given_and_last,
        (True, True, False, True): _from_given_and_last,
        (True, True, False, False): _from_given_and_last,
        (True, False, True, True): _from_name,
        (True, False, True, False): _from_alias,
        (True, False, False, True): _from_name,
        (True, False, False, False): _from_given_only,
        (False, True, True, True): _from_last_only,
        (False, True, True, False): _from_last_only,
        (False, True, False, True): _from_last_only,
        (False, True, False, False): _from_last_only,
        (False, False, True, True): _from_name,
        (False, False, True, False): _from_alias,
        (False, False, False, True): _from_name,
        (False, False, False, False): _from_thin_air
    }[(has_given_names, has_family_names, has_alias, has_name)](author_cff)


def _exists_nonempty(obj, key):
    value = obj.get(key, None)
    return value is not None and value != ''


def _from_alias(author_cff):
    return author_cff.get('alias')


def _from_given_and_last(author_cff):
    return _from_last_only(author_cff) + ", " + _from_given_only(author_cff)


def _from_given_only(author_cff):
    return author_cff.get('given-names')


def _from_last_only(author_cff):
    nameparts = [
        author_cff.get('name-particle'),
        author_cff.get('family-names'),
        author_cff.get('name-suffix')
    ]
    return ' '.join([n for n in nameparts if n is not None])


def _from_name(author_cff):
    return author_cff.get('name')


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

    def add_author(self):
        authors_cff = self.cffobj.get('authors', list())
        authors_bibtex = [_author_cff_to_author_bibtex(a) for a in authors_cff]
        self.author = 'author = {' + ' and '.join([a for a in authors_bibtex if a is not None]) + '}'
        return self

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
