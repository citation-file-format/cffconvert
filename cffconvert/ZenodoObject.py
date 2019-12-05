class ZenodoObject:
    def __init__(self, cff_object):
        if 'cff-version' in cff_object.keys():
            self.cff_object = cff_object
            self.cff_version = cff_object['cff-version']
        else:
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        self.creators = None
        self.doi = None
        self.keywords = None
        self.license = None
        self.publication_date = None
        self.title = None
        self.version = None

    def add_creators(self):
        if 'authors' in self.cff_object.keys():
            self.creators = list()
            for author in self.cff_object['authors']:
                d = dict()
                keys = author.keys()
                nameparts = [
                    author['name-particle'] if 'name-particle' in keys else None,
                    author['family-names'] if 'family-names' in keys else None,
                    author['name-suffix'] if 'name-suffix' in keys else None
                ]
                tmp = ' '.join([namepart for namepart in nameparts if namepart is not None])
                fullname = tmp + ', ' + author['given-names'] if 'given-names' in keys else tmp
                if fullname != '':
                    d['name'] = fullname
                elif 'alias' in keys and author['alias'] is not None and author['alias'] != '':
                    d['name'] = author['alias']
                else:
                    continue
                if 'affiliation' in author.keys():
                    d['affiliation'] = author['affiliation']
                self.creators.append(d)

    def add_doi(self):
        version = self.cff_version
        if version in ['1.0.3', '1.1.0']:
            if 'doi' in self.cff_object.keys():
                self.doi = self.cff_object['doi']

        if version in ['1.1.0']:
            if 'identifiers' in self.cff_object.keys():
                identifiers = self.cff_object['identifiers']
                for identifier in identifiers:
                    if identifier['type'] == 'doi':
                        self.doi = identifier['value']
                        break
        return self

    def add_keywords(self):
        if 'keywords' in self.cff_object.keys():
            self.keywords = self.cff_object['keywords']

    def add_license(self):
        if 'license' in self.cff_object.keys():
            self.license = dict(id=self.cff_object['license'])

    def add_publication_date(self):
        if 'date-released' in self.cff_object.keys():
            self.publication_date = '{:d}-{:02d}-{:02d}'.format(self.cff_object['date-released'].year,
                                                                self.cff_object['date-released'].month,
                                                                self.cff_object['date-released'].day)

    def add_title(self):
        if 'title' in self.cff_object.keys():
            self.title = self.cff_object['title']
        return self

    def add_version(self):
        if 'version' in self.cff_object.keys():
            self.version = self.cff_object['version']
        return self


