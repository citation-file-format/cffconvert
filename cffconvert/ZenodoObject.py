import json


class ZenodoObject:

    supported_cff_versions = ['1.0.3', '1.1.0']

    def __init__(self, cff_object, initialize_empty=False):
        if 'cff-version' in cff_object.keys():
            if cff_object['cff-version'] not in ZenodoObject.supported_cff_versions:
                raise ValueError('\'cff-version\': {} isn\'t a supported version.'.format(cff_object['cff-version']))
            self.cff_object = cff_object
        else:
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        self.creators = None
        self.doi = None
        self.keywords = None
        self.license = None
        self.publication_date = None
        self.title = None
        self.version = None
        if initialize_empty:
            pass
        else:
            self.add_all()

    def __str__(self):
        d = {
            "creators": self.creators,
            "doi": self.doi,
            "keywords": self.keywords,
            "license": self.license,
            "publication_date": self.publication_date,
            "title": self.title,
            "version": self.version
        }
        filtered = [item for item in d.items() if item[1] is not None]
        return json.dumps(dict(filtered), sort_keys=True, indent=3, separators=(', ', ': '), ensure_ascii=False) + '\n'

    def add_all(self):
        self.add_creators()          \
            .add_doi()               \
            .add_keywords()          \
            .add_license()           \
            .add_publication_date()  \
            .add_title()             \
            .add_version()

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
                if 'orcid' in author.keys():
                    if author['orcid'].startswith('https://orcid.org/'):
                        d['orcid'] = author['orcid'][len('https://orcid.org/'):]

                self.creators.append(d)
        return self

    def add_doi(self):
        version = self.cff_object['cff-version']
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
        return self

    def add_license(self):
        if 'license' in self.cff_object.keys():
            self.license = dict(id=self.cff_object['license'])
        return self

    def add_publication_date(self):
        if 'date-released' in self.cff_object.keys():
            self.publication_date = '{:d}-{:02d}-{:02d}'.format(self.cff_object['date-released'].year,
                                                                self.cff_object['date-released'].month,
                                                                self.cff_object['date-released'].day)
        return self

    def add_title(self):
        if 'title' in self.cff_object.keys():
            self.title = self.cff_object['title']
        return self

    def add_version(self):
        if 'version' in self.cff_object.keys():
            self.version = self.cff_object['version']
        return self

    def print(self):
        return self.__str__()


