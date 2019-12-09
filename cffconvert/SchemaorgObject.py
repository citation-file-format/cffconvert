import json


class SchemaorgObject:

    supported_cff_versions = ['1.0.3', '1.1.0']
    supported_schemaorg_props = ['codeRepository']

    def __init__(self, cff_object, initialize_empty=False):
        self.cff_object = cff_object
        self.code_repository = None
        if initialize_empty:
            pass
        else:
            self.check_cff_object().add_all()

    def __str__(self):
        d = {
            "@context": "https://schema.org",
            "@type": "SoftwareSourceCode",
            "codeRepository": self.code_repository
        }
        filtered = [item for item in d.items() if item[1] is not None]
        return json.dumps(dict(filtered), sort_keys=True, indent=3,
                          separators=(', ', ': '), ensure_ascii=False) + '\n'

    def add_all(self):
        self.add_code_repository()
        return self

    def add_code_repository(self):
        if 'repository-code' in self.cff_object.keys():
            self.code_repository = self.cff_object['repository-code']
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


