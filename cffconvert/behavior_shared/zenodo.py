import json
from abc import abstractmethod


class ZenodoObjectShared:

    supported_zenodo_props = [
        'creators',
        'description',
        'keywords',
        'license',
        'publication_date',
        'title',
        'version'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        self.cffobj = cffobj
        self.creators = None
        self.description = None
        self.keywords = None
        self.license = None
        self.publication_date = None
        self.title = None
        self.version = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def __str__(self):
        d = {
            "creators": self.creators,
            "description": self.description,
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
            .add_description()       \
            .add_keywords()          \
            .add_license()           \
            .add_publication_date()  \
            .add_title()             \
            .add_version()
        return self

    def add_creators(self):
        if 'authors' in self.cffobj.keys():
            self.creators = list()
            for author in self.cffobj['authors']:
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

    def add_description(self):
        if 'abstract' in self.cffobj.keys():
            self.description = self.cffobj['abstract']
        return self

    def add_keywords(self):
        if 'keywords' in self.cffobj.keys():
            self.keywords = self.cffobj['keywords']
        return self

    def add_license(self):
        if 'license' in self.cffobj.keys():
            self.license = dict(id=self.cffobj['license'])
        return self

    @abstractmethod
    def add_publication_date(self):
        pass

    def add_title(self):
        if 'title' in self.cffobj.keys():
            self.title = self.cffobj['title']
        return self

    def add_version(self):
        if 'version' in self.cffobj.keys():
            self.version = self.cffobj['version']
        return self

    @abstractmethod
    def check_cffobj(self):
        pass

    def print(self):
        return self.__str__()
