import json
from abc import abstractmethod


class SchemaorgObjectShared:

    supported_schemaorg_props = [
        'author',
        'codeRepository',
        'datePublished',
        'description',
        'identifier',
        'keywords',
        'license',
        'name',
        'version'
    ]

    def __init__(self, cffobj, initialize_empty=False, context="https://schema.org"):
        self.cffobj = cffobj
        self.author = None
        self.code_repository = None
        self.date_published = None
        self.description = None
        self.identifier = None
        self.keywords = None
        self.license = None
        self.name = None
        self.version = None
        self.context = context
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def __str__(self):
        d = {
            "@context": self.context,
            "@type": "SoftwareSourceCode",
            "author": self.author,
            "codeRepository": self.code_repository,
            "datePublished": self.date_published,
            "description": self.description,
            "identifier": self.identifier,
            "keywords": self.keywords,
            "license": self.license,
            "name": self.name,
            "version": self.version
        }
        filtered = [item for item in d.items() if item[1] is not None]
        return json.dumps(dict(filtered), sort_keys=True, indent=3,
                          separators=(', ', ': '), ensure_ascii=False) + '\n'

    def add_all(self):
        self.add_author()           \
            .add_code_repository()  \
            .add_date_published()   \
            .add_description()      \
            .add_identifier()       \
            .add_keywords()         \
            .add_license()          \
            .add_name()             \
            .add_version()
        return self

    def add_author(self):
        if 'authors' in self.cffobj.keys():
            self.author = list()
            for author in self.cffobj['authors']:
                d = dict()
                keys = author.keys()
                if 'orcid' in author.keys():
                    if author['orcid'].startswith('https://orcid.org/'):
                        d['@id'] = author['orcid']
                d["@type"] = "Person"
                if 'affiliation' in author.keys():
                    d['affiliation'] = {
                        "@type": "Organization",
                        "legalName": author['affiliation']
                    }
                nameparts = [
                    author['name-particle'] if 'name-particle' in keys else None,
                    author['family-names'] if 'family-names' in keys else None,
                    author['name-suffix'] if 'name-suffix' in keys else None
                ]
                family_name = ' '.join([namepart for namepart in nameparts if namepart is not None])
                given_name = author['given-names'] if 'given-names' in keys and             \
                                                      author['given-names'] is not None and \
                                                      author['given-names'] != '' else None
                alias = author['alias'] if 'alias' in keys and             \
                                           author['alias'] is not None and \
                                           author['alias'] != '' else None
                if family_name or given_name:
                    if family_name:
                        d['familyName'] = family_name
                    if given_name:
                        d['givenName'] = given_name
                elif alias:
                    d['name'] = alias
                else:
                    continue
                self.author.append(d)
        return self

    def add_code_repository(self):
        if 'repository-code' in self.cffobj.keys():
            self.code_repository = self.cffobj['repository-code']
        return self

    @abstractmethod
    def add_date_published(self):
        pass

    def add_description(self):
        if 'abstract' in self.cffobj.keys():
            self.description = self.cffobj['abstract']
        return self

    @abstractmethod
    def add_identifier(self):
        pass

    def add_keywords(self):
        if 'keywords' in self.cffobj.keys():
            self.keywords = self.cffobj['keywords']
        return self

    def add_license(self):
        if 'license' in self.cffobj.keys():
            self.license = 'https://spdx.org/licenses/{}'.format(self.cffobj['license'])
        return self

    def add_name(self):
        if 'title' in self.cffobj.keys():
            self.name = self.cffobj['title']
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
