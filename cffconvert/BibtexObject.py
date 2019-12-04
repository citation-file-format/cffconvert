class BibtexObject:
    def __init__(self, cff_object, reference='YourReferenceHere'):
        if 'cff-version' in cff_object.keys():
            self.cff_object = cff_object
            self.cff_version = cff_object['cff-version']
        else:
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        self.reference = reference
        self.author = None
        self.doi = None
        self.month = None
        self.title = None
        self.url = None
        self.year = None

    def add_author(self):
        if 'authors' in self.cff_object.keys():
            for author in self.cff_object.authors:
                pass

    def add_doi(self):
        version = self.cff_version
        if version in ['1.0.3', '1.1.0']:
            if 'doi' in self.cff_object.keys():
                self.doi = 'doi = {' + self.cff_object['doi'] + '}\n'

        if version in ['1.1.0']:
            if 'identifiers' in self.cff_object.keys():
                identifiers = self.cff_object['identifiers']
                for identifier in identifiers:
                    if identifier['type'] == 'doi':
                        self.doi = 'doi = {' + identifier['value'] + '}\n'
                        break
        return self

    def add_month(self):
        if 'date-released' in self.cff_object.keys():
            self.month = 'month = {' + str(self.cff_object['date-released'].month) + '}\n'

    def add_title(self):
        if 'title' in self.cff_object.keys():
            self.title = 'title = {' + self.cff_object['title'] + '}\n'
        return self

    def add_url(self):
        if 'repository-code' in self.cff_object.keys():
            self.url = 'url = {' + self.cff_object['repository-code'] + '}\n'

    def add_year(self):
        if 'date-released' in self.cff_object.keys():
            self.year = 'year = {' + str(self.cff_object['date-released'].year) + '}\n'

    def __str__(self):
        items = [item for item in [self.author,
                                   self.title,
                                   self.month,
                                   self.year,
                                   self.doi,
                                   self.url] if item is not None]
        s = ', '.join(items)
        return '@misc{' + self.reference + ',\n' + s + '}\n'

    def print(self):
        return self.__str__()