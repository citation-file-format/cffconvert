class ApalikeObject:

    supported_cff_versions = ['1.0.3', '1.1.0']
    supported_pure_props = ['author', 'year', 'title', 'doi', 'url']

    def __init__(self, cff_object, initialize_empty=False):
        self.cff_object = cff_object
        self.author = None
        self.year = None
        self.title = None
        self.doi = None
        self.url = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cff_object().add_all()

    def __str__(self):
        items = [item for item in [self.author,
                                   self.year,
                                   self.title,
                                   self.doi,
                                   self.url] if item is not None]
        return ''.join(items)

    def add_all(self):
        self.add_author()   \
            .add_year()     \
            .add_title()    \
            .add_doi()      \
            .add_url()
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
                    authors.append(format(fullname))
                elif alias:
                    authors.append(format(alias))
                else:
                    continue
            self.author = ''.join(authors)
        return self

    def add_year(self):
        if 'date-released' in self.cff_object.keys():
            self.year = ' (' + str(self.cff_object['date-released'].year) + '). '
        return self

    def add_title(self):
        if 'title' in self.cff_object.keys():
            self.title = format(self.cff_object['title']) + '. '
        return self

    def add_doi(self):
        version = self.cff_object['cff-version']
        if version in ['1.0.3', '1.1.0']:
            if 'doi' in self.cff_object.keys():
                self.doi = 'doi: ' + format(self.cff_object['doi']) + '. '

        if version in ['1.1.0']:
            if 'identifiers' in self.cff_object.keys():
                identifiers = self.cff_object['identifiers']
                for identifier in identifiers:
                    if identifier['type'] == 'doi':
                        self.doi = 'doi: ' + format(identifier['value']) + '. '
                        break
        return self

    def add_url(self):
        if 'repository-code' in self.cff_object.keys():
            self.url = format(self.cff_object['repository-code']) + '\n'
        return self

    def check_cff_object(self):
        if not isinstance(self.cff_object, dict):
            raise ValueError('Expected cff_object to be of type \'dict\'.')
        elif 'cff-version' not in self.cff_object.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        elif self.cff_object['cff-version'] not in ApalikeObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cff_object['cff-version']))
        else:
            return self

    def print(self):
        return self.__str__()

