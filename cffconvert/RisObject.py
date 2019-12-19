class RisObject:

    supported_cff_versions = ['1.0.3', '1.1.0']
    supported_ris_props = ['abstract', 'author', 'date', 'doi', 'keywords',
                           'title', 'url', 'year']

    def __init__(self, cff_object, initialize_empty=False):
        self.cff_object = cff_object
        self.abstract = None
        self.author = None
        self.date = None
        self.doi = None
        self.keywords = None
        self.title = None
        self.url = None
        self.year = None
        if initialize_empty:
            pass
        else:
            self.check_cff_object().add_all()

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
        if 'abstract' in self.cff_object.keys():
            self.abstract = 'AB  - {}\n'.format(self.cff_object['abstract'])
        return self

    def add_author(self):
        if 'authors' in self.cff_object.keys():
            authors = list()
            for author in self.cff_object['authors']:
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
                    authors.append('AU  - {}\n'.format(fullname))
                elif alias:
                    authors.append('AU  - {}\n'.format(alias))
                else:
                    continue
            self.author = ''.join(authors)
        return self

    def add_date(self):
        if 'date-released' in self.cff_object.keys():
            self.date = "DA  - {:d}-{:02d}-{:02d}\n".format(self.cff_object['date-released'].year,
                                                            self.cff_object['date-released'].month,
                                                            self.cff_object['date-released'].day)
        return self

    def add_doi(self):
        version = self.cff_object['cff-version']
        if version in ['1.0.3', '1.1.0']:
            if 'doi' in self.cff_object.keys():
                self.doi = 'DO  - {}\n'.format(self.cff_object['doi'])

        if version in ['1.1.0']:
            if 'identifiers' in self.cff_object.keys():
                identifiers = self.cff_object['identifiers']
                for identifier in identifiers:
                    if identifier['type'] == 'doi':
                        self.doi = 'DO  - {}\n'.format(identifier['value'])
                        break
        return self

    def add_keywords(self):
        if 'keywords' in self.cff_object.keys():
            keywords = ['KW  - {}\n'.format(keyword) for keyword in self.cff_object['keywords']]
            self.keywords = ''.join(keywords)
        return self

    def add_title(self):
        if 'title' in self.cff_object.keys():
            self.title = 'TI  - {}\n'.format(self.cff_object['title'])
        return self

    def add_url(self):
        if 'repository-code' in self.cff_object.keys():
            self.url = 'UR  - {}\n'.format(self.cff_object['repository-code'])
        return self

    def add_year(self):
        if 'date-released' in self.cff_object.keys():
            self.year = 'PY  - {}\n'.format(self.cff_object['date-released'].year)
        return self

    def check_cff_object(self):
        if not isinstance(self.cff_object, dict):
            raise ValueError('Expected cff_object to be of type \'dict\'.')
        elif 'cff-version' not in self.cff_object.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        elif self.cff_object['cff-version'] not in RisObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cff_object['cff-version']))
        else:
            return self

    def print(self):
        return self.__str__()

