class BibtexObject:

    supported_bibtex_props = [
        'author',
        'doi',
        'month',
        'title',
        'url',
        'year'
    ]
    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
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
        if 'authors' in self.cffobj.keys():
            fullnames = []
            for author in self.cffobj['authors']:
                keys = author.keys()
                nameparts = [
                    author['given-names'] if 'given-names' in keys else None,
                    author['name-particle'] if 'name-particle' in keys else None,
                    author['family-names'] if 'family-names' in keys else None,
                    author['name-suffix'] if 'name-suffix' in keys else None
                ]
                fullname = ' '.join([namepart for namepart in nameparts if namepart is not None])
                if fullname == '' and 'alias' in keys and author['alias'] is not None:
                    fullname = author['alias'] if author['alias'] != '' else None
                if fullname is not None and fullname != '':
                    fullnames.append(fullname)
            self.author = 'author = {' + ' and '.join(fullnames) + '}'
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = 'doi = {' + self.cffobj['doi'] + '}'
        return self

    def add_month(self):
        if 'date-released' in self.cffobj.keys():
            self.month = 'month = {' + str(self.cffobj['date-released'].month) + '}'
        return self

    def add_title(self):
        if 'title' in self.cffobj.keys():
            self.title = 'title = {' + self.cffobj['title'] + '}'
        return self

    def add_url(self):
        if 'repository-code' in self.cffobj.keys():
            self.url = 'url = {' + self.cffobj['repository-code'] + '}'
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = 'year = {' + str(self.cffobj['date-released'].year) + '}'
        return self

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError('Expected cffobj to be of type \'dict\'.')
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        if self.cffobj['cff-version'] not in BibtexObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cffobj['cff-version']))

    def print(self, reference='YourReferenceHere'):
        return self.__str__(reference)
