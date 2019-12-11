import json
from cffconvert.SchemaorgObject import SchemaorgObject


class CodemetaObject(SchemaorgObject):

    supported_cff_versions = ['1.0.3', '1.1.0']
    supported_codemeta_props = ['author', 'codeRepository', 'datePublished', 'description',
                                'identifier', 'keywords', 'license', 'name', 'version']

    def __init__(self, cff_object, initialize_empty=False):
        super().__init__(cff_object, initialize_empty)
        if initialize_empty:
            pass
        else:
            self.check_cff_object().add_all()

    def __str__(self):
        d = {
            "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
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

