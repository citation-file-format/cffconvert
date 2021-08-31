class EndnoteObject:

    supported_cff_versions = ['1.0.3', '1.1.0', '1.2.0']
    supported_endnote_props = ['author', 'year', 'keyword', 'doi', 'name', 'url']

    def __init__(self, cff_object, initialize_empty=False):
        self.cff_object = cff_object
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
            self.check_cff_object().add_all()

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
                    authors.append('%A {}\n'.format(fullname))
                elif alias:
                    authors.append('%A {}\n'.format(alias))
                else:
                    continue
            self.author = ''.join(authors)
        return self

    def add_doi(self):
        version = self.cff_object['cff-version']
        if version in ['1.0.3', '1.1.0', '1.2.0']:
            if 'doi' in self.cff_object.keys():
                self.doi = '%R {}\n'.format(self.cff_object['doi'])

        if version in ['1.1.0', '1.2.0']:
            if 'identifiers' in self.cff_object.keys():
                identifiers = self.cff_object['identifiers']
                for identifier in identifiers:
                    if identifier['type'] == 'doi':
                        self.doi = '%R {}\n'.format(identifier['value'])
                        break
        return self

    def add_keyword(self):
        if 'keywords' in self.cff_object.keys():
            keywords = ['%K {}\n'.format(keyword) for keyword in self.cff_object['keywords']]
            self.keyword = ''.join(keywords)
        return self

    def add_name(self):
        if 'title' in self.cff_object.keys():
            self.name = '%T {}\n'.format(self.cff_object['title'])
        return self

    def add_url(self):
        if 'repository-code' in self.cff_object.keys():
            self.url = '%U {}\n'.format(self.cff_object['repository-code'])
        return self

    def add_year(self):
        version = self.cff_object['cff-version']
        if version in ['1.0.1', '1.0.2', '1.0.3', '1.1.0']:
            if 'date-released' in self.cff_object.keys():
                self.year = '%D {}\n'.format(self.cff_object['date-released'].year)
        elif version in ['1.2.0']:
            if 'date-released' in self.cff_object.keys():
                self.year = '%D {}\n'.format(self.cff_object['date-released'][:4])
        else:
            raise ValueError("Unsupported schema version")
        return self

    def check_cff_object(self):
        if not isinstance(self.cff_object, dict):
            raise ValueError('Expected cff_object to be of type \'dict\'.')
        elif 'cff-version' not in self.cff_object.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        elif self.cff_object['cff-version'] not in EndnoteObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cff_object['cff-version']))
        else:
            return self

    def print(self):
        return self.__str__()
