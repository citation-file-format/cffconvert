import json


class SchemaorgObject:

    supported_cff_versions = ['1.0.3', '1.1.0']
    supported_schemaorg_props = ['author', 'codeRepository', 'datePublished', 'description',
                                 'identifier', 'keywords', 'license', 'name', 'version']

    def __init__(self, cff_object, initialize_empty=False):
        self.cff_object = cff_object
        self.author = None
        self.code_repository = None
        self.date_published = None
        self.description = None
        self.identifier = None
        self.keywords = None
        self.license = None
        self.name = None
        self.version = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cff_object().add_all()

    def __str__(self):
        d = {
            "@context": "https://schema.org",
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
        if 'authors' in self.cff_object.keys():
            self.author = list()
            for author in self.cff_object['authors']:
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
        if 'repository-code' in self.cff_object.keys():
            self.code_repository = self.cff_object['repository-code']
        return self

    def add_date_published(self):
        if 'date-released' in self.cff_object.keys():
            self.date_published = "{:d}-{:02d}-{:02d}".format(self.cff_object['date-released'].year,
                                                              self.cff_object['date-released'].month,
                                                              self.cff_object['date-released'].day)
        return self

    def add_description(self):
        if 'abstract' in self.cff_object.keys():
            self.description = self.cff_object['abstract']
        return self

    def add_identifier(self):
        version = self.cff_object['cff-version']
        if version in ['1.0.3', '1.1.0']:
            if 'doi' in self.cff_object.keys():
                self.identifier = 'https://doi.org/{}'.format(self.cff_object['doi'])

        if version in ['1.1.0']:
            if 'identifiers' in self.cff_object.keys():
                identifiers = self.cff_object['identifiers']
                for identifier in identifiers:
                    if identifier['type'] == 'doi':
                        self.identifier = 'https://doi.org/{}'.format(identifier['value'])
                        break
        return self

    def add_keywords(self):
        if 'keywords' in self.cff_object.keys():
            self.keywords = self.cff_object['keywords']
        return self

    def add_license(self):
        if 'license' in self.cff_object.keys():
            self.license = 'https://spdx.org/licenses/{}'.format(self.cff_object['license'])
        return self

    def add_name(self):
        if 'title' in self.cff_object.keys():
            self.name = self.cff_object['title']
        return self

    def add_version(self):
        if 'version' in self.cff_object.keys():
            self.version = self.cff_object['version']
        return self

    def check_cff_object(self):
        if not isinstance(self.cff_object, dict):
            raise ValueError('Expected cff_object to be of type \'dict\'.')
        elif 'cff-version' not in self.cff_object.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        elif self.cff_object['cff-version'] not in SchemaorgObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cff_object['cff-version']))
        else:
            return self

    def print(self):
        return self.__str__()


